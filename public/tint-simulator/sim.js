(function(){
var API='https://tintsquad-tintsim-api.onrender.com', PAGE=location.origin+'/tint-simulator';
var $=function(id){return document.getElementById(id)}, D=null, f=$('sim'), imgUrl='';
fetch(API+'/health').catch(function(){}); // wake the server early
function opts(sel,list,ph){sel.innerHTML='<option value="">'+ph+'</option>'+list.map(function(o){return '<option value="'+o[0]+'">'+o[1]+'</option>'}).join('');sel.disabled=!list.length}
function shades(sel,list){sel.innerHTML='<option value="" selected>None</option>'+list.map(function(s){return '<option>'+s+'</option>'}).join('');sel.value=''}
function resetShades(){['front','rear','back','full'].forEach(function(k){shades($(k),D.shades[k])});$('strip').checked=false}
fetch('/tint-simulator/data.json').then(function(r){return r.json()}).then(function(d){D=d;
  opts($('year'),d.years.map(function(y){return [y,y]}),'Year');
  opts($('make'),Object.keys(d.vehicles).map(function(m){return [m,m]}),'Make');resetShades();});
$('make').onchange=function(){var m=this.value,ms=m?Object.keys(D.vehicles[m]):[];opts($('model'),ms.map(function(x){return [x,x]}),'Model');
  var c=(D.colors[m]||[]).concat(D.colors['*']||[]);opts($('color'),c,'Paint color');$('bodyw').hidden=true;opts($('body'),[],'')};
$('model').onchange=function(){var b=this.value?D.vehicles[$('make').value][this.value]:[];
  opts($('body'),b.map(function(x){return [x[0],x[1]||'Standard']}),'Body style');
  if(b.length===1){$('body').value=b[0][0];$('bodyw').hidden=true}else{$('bodyw').hidden=!b.length}};
f.onsubmit=function(e){e.preventDefault();var err=$('err');err.textContent='';
  var body={year:$('year').value,vehicleId:$('body').value,colorId:$('color').value,front:$('front').value,rear:$('rear').value,back:$('back').value,full:$('full').value,strip:$('strip').checked};
  if(!body.year||!body.vehicleId||!body.colorId){err.textContent='Please pick your year, vehicle and paint color.';return}
  if(!body.front&&!body.rear&&!body.back&&!body.full&&!body.strip){err.textContent='Pick a shade for at least one window.';return}
  var btn=$('go');btn.disabled=true;btn.textContent='Creating your preview…';$('out').hidden=false;$('wait').hidden=false;$('res').hidden=true;$('sharemenu').hidden=true;
  var t=Date.now(),tick=setInterval(function(){$('secs').textContent=Math.round((Date.now()-t)/1000)},500);
  fetch(API+'/render',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}).then(function(r){return r.json().then(function(j){if(!r.ok)throw new Error(j.error||'Something went wrong');return j})})
  .then(function(j){imgUrl=j.image;var img=$('img');img.onload=function(){clearInterval(tick);$('wait').hidden=true;$('res').hidden=false;$('res').scrollIntoView({behavior:'smooth',block:'start'})};img.src=imgUrl;
    $('cap').textContent=$('year').value+' '+$('make').value+' '+$('model').value+' · '+$('color').selectedOptions[0].text+' · fronts '+(body.front||'none')+', rears '+(body.rear||'none')+', back glass '+(body.back||'none')+(body.full?', windshield '+body.full:'')+(body.strip?', windshield strip':'');
    var txt='Check out my tint preview from Tint Squad in Syracuse!';
    $('sh-fb').href='https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(imgUrl);
    $('sh-x').href='https://twitter.com/intent/tweet?text='+encodeURIComponent(txt)+'&url='+encodeURIComponent(imgUrl);
    $('sh-dl').href=imgUrl;})
  .catch(function(x){clearInterval(tick);$('out').hidden=true;err.textContent=x.message})
  .finally(function(){btn.disabled=false;btn.textContent='Show My Tint'});};
$('share').onclick=function(){var txt='Check out my tint preview from Tint Squad in Syracuse!';
  if(navigator.share&&navigator.canShare){fetch(imgUrl).then(function(r){return r.blob()}).then(function(b){var file=new File([b],'my-tint-preview.jpg',{type:'image/jpeg'});
    var data={files:[file],title:'My tint preview',text:txt+' '+PAGE};
    if(navigator.canShare(data))return navigator.share(data);return navigator.share({title:'My tint preview',text:txt,url:imgUrl})})
   .catch(function(e){if(e&&e.name!=='AbortError')$('sharemenu').hidden=false});}
  else $('sharemenu').hidden=!$('sharemenu').hidden;};
$('sh-copy').onclick=function(){var b=this;(navigator.clipboard?navigator.clipboard.writeText(imgUrl):Promise.reject()).then(function(){b.textContent='Copied!'},function(){prompt('Copy this link:',imgUrl)})};
$('sh-dl').onclick=function(e){e.preventDefault();fetch(imgUrl).then(function(r){return r.blob()}).then(function(b){var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='my-tint-preview.jpg';document.body.appendChild(a);a.click();a.remove()}).catch(function(){window.open(imgUrl,'_blank')})};
$('again').onclick=function(){f.reset();resetShades();$('make').onchange.call($('make'));$('out').hidden=true;$('sharemenu').hidden=true;$('err').textContent='';$('bodyw').hidden=true;imgUrl='';window.scrollTo({top:f.offsetTop-80,behavior:'smooth'})};
})();
