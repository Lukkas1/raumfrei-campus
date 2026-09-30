(function(root){
const min=t=>{const [h,m]=t.split(':').map(Number);return h*60+m};
const hhmm=m=>`${String(Math.floor(m/60)).padStart(2,'0')}:${String(m%60).padStart(2,'0')}`;
function berlin(now=new Date()){const p=Object.fromEntries(new Intl.DateTimeFormat('sv-SE',{timeZone:'Europe/Berlin',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hourCycle:'h23'}).formatToParts(now).map(x=>[x.type,x.value]));return {date:`${p.year}-${p.month}-${p.day}`,minute:Number(p.hour)*60+Number(p.minute)}}
function weekday(date){return new Date(date+'T12:00:00Z').getUTCDay()||7}
function events(room,date){return room.events.filter(e=>e.day===weekday(date))}
function segments(room,date){const es=events(room,date),end=min(room.coverageEnd);const edges=[...new Set([480,1200,end,...es.flatMap(e=>[min(e.start),min(e.end)])])].filter(n=>n>=480&&n<=1200).sort((a,b)=>a-b);return edges.slice(0,-1).map((start,i)=>{const stop=edges[i+1],e=es.find(e=>min(e.start)<=start&&min(e.end)>start);let type=weekday(date)>5?'unknown':e?(e.uncertain?'uncertain':'busy'):start>=end?'unknown':'free';return {start,end:stop,type,event:e}})}
function status(room,date,t){if(t<480||t>=1200||weekday(date)>5)return {type:'unknown',label:'Keine Plandaten'};const ss=segments(room,date),i=ss.findIndex(s=>t>=s.start&&t<s.end),s=ss[i];let end=s.end;for(let j=i+1;j<ss.length&&ss[j].type===s.type;j++)end=ss[j].end;const next=ss.slice(i+1).find(x=>x.type==='free');return {...s,end,remaining:end-t,nextFree:next?.start,tentative:room.tentative}}
const api={min,hhmm,berlin,weekday,events,segments,status};root.RoomEngine=api;if(typeof module!=='undefined')module.exports=api;
})(typeof window==='undefined'?globalThis:window);
