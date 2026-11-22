from common import ROOT,save,sha
import source,json,argparse,concurrent.futures,time

def capture():
 raw=source.get(source.OIC+'/en/decisions?page=0');rows,last,expected=source.parse_oic(raw)
 def page(item):
  index,ascending=item;time.sleep(.3);url=source.OIC+'/en/decisions?'+('sort_bef_combine=field_release_date_ASC&' if ascending else '')+'page='+str(index)
  r,_,n=source.parse_oic(source.get(url))
  if not r or n!=expected:raise ValueError('Decision pagination changed during capture')
  return r
 with concurrent.futures.ThreadPoolExecutor(3) as pool:
  for part in pool.map(page,[(i,False) for i in range(1,last+1)]):rows+=part
 unique={r['id']:r for r in rows}
 if len(unique)<expected:
  with concurrent.futures.ThreadPoolExecutor(3) as pool:
   for part in pool.map(page,[(i,True) for i in range(last+1)]):
    for r in part:unique[r['id']]=r
 if len(unique)<expected*.95:raise ValueError('Large source pagination gap; retain prior dataset')
 # Fresh final-report date index, no persistent HTTP cache across runs.
 (source.ROOT/'final-reports.html').unlink(missing_ok=True);dates=source.decision_dates()
 for r in unique.values():r['decision_date']=dates.get(r['source_url'])
 return {'rows':list(unique.values()),'source_reported_count':expected}

def main():
 p=argparse.ArgumentParser();p.add_argument('--seed',action='store_true');a=p.parse_args()
 d=json.loads((source.ROOT/'atipdecisions.json').read_text()) if a.seed else capture();rows=d['rows'];expected=d.get('source_reported_count',d.get('expected_count',len(rows)))
 for r in rows:r['year']=r['listing_date'][:4];r['issues']=sorted(set(r['issues']+['Act section '+s for s in r['sections']]))
 warnings=['Selected published reports are not the complete universe of access complaints. Issue tags are summary-keyword aids; original reports control interpretation.']
 if len(rows)!=expected:warnings.append(f'The source reports {expected:,} decisions but pagination yielded {len(rows):,} distinct IDs; the coverage gap remains visible.')
 save(rows,sources=[{'label':'Information Commissioner decisions','url':source.OIC+'/en/decisions'},{'label':'Final reports and decision dates','url':source.OIC+'/en/decisions/final-reports'},{'label':'Quarterly complaint statistics (different denominator)','url':source.OIC+'/en/information-commissioners-guidance/quarterly-statistics'}],coverage=f"{len(rows):,} distinct published decisions · source reports {expected:,} · listing dates {min(r['listing_date'] for r in rows)} to {max(r['listing_date'] for r in rows)}",warnings=warnings,extra={'source_reported_count':expected,'coverage_complete':len(rows)==expected})
if __name__=='__main__':main()
