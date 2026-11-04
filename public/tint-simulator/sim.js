(function(){
var API='https://tintsquad-tintsim-api.onrender.com', BOOK='https://tint-squad.onrender.com/book/';
var $=function(id){return document.getElementById(id)}, D=null, f=$('sim');
fetch(API+'/health').catch(function(){}); // wake the server while the visitor fills the form
function opts(sel,list,ph){sel.innerHTML='<option value="">'+ph+'</option>'+list.map(function(o){return '<option value="'+o[0]+'">'+o[1]+'</option>'}).join('');sel.disabled=!list.length}
function shades(sel,list,none){sel.innerHTML='<option value="">'+none+'</option>'+list.map(function(s){return '<option>'+s+'</option>'}).join('')}
fetch('/tint-simulator/data.json').then(function(r){return r.json()}).then(function(d){D=d;
  opts($('year'),d.years.map(function(y){return [y,y]}),'Year');
  opts($('make'),Object.keys(d.vehicles).map(function(m){return [m,m]}),'Make');
  shades($('front'),d.shades.front,'No tint (factory)');shades($('rear'),d.shades.rear,'No tint (factory)');
  shades($('back'),d.shades.back,'No tint (factory)');shades($('full'),d.shades.full,'No full windshield');
  $('front').value=d.shades.front.indexOf('20%')>=0?'20%':'';
  $('make').disabled=false;});
$('make').onchange=function(){var m=this.value,ms=m?Object.keys(D.vehicles[m]):[];opts($('model'),ms.map(function(x){return [x,x]}),'Model');
  var c=(D.colors[m]||[]).concat(D.colors['*']||[]);opts($('color'),c,'Paint color');$('bodyw').hidden=true;opts($('body'),[],'')};
$('model').onchange=function(){var b=this.value?D.vehicles[$('make').value][this.value]:[];
  opts($('body'),b.map(function(x){return [x[0],x[1]||'Standard']}),'Body style');
  if(b.length===1){$('body').value=b[0][0];$('bodyw').hidden=true}else{$('bodyw').hidden=!b.length}};
f.onsubmit=function(e){e.preventDefault();var err=$('err');err.textContent='';
  var body={year:$('year').value,vehicleId:$('body').value,colorId:$('color').value,front:$('front').value,rear:$('rear').value,back:$('back').value,full:$('full').value,strip:$('strip').checked,name:$('name').value,phone:$('phone').value,website:$('website').value};
  if(!body.year||!body.vehicleId||!body.colorId){err.textContent='Please pick your year, vehicle and paint color.';return}
  var btn=$('go');btn.disabled=true;btn.textContent='Creating your preview…';$('out').hidden=false;$('wait').hidden=false;$('res').hidden=true;
  var t=Date.now(),tick=setInterval(function(){$('secs').textContent=Math.round((Date.now()-t)/1000)},500);
  fetch(API+'/render',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}).then(function(r){return r.json().then(function(j){if(!r.ok)throw new Error(j.error||'Something went wrong');return j})})
  .then(function(j){var img=$('img');img.onload=function(){clearInterval(tick);$('wait').hidden=true;$('res').hidden=false;$('res').scrollIntoView({behavior:'smooth',block:'start'})};img.src=j.image;
    var sel=$('body');$('cap').textContent=$('year').value+' '+$('make').value+' '+$('model').value+' · '+$('color').selectedOptions[0].text+' · fronts '+(body.front||'factory')+', rears '+(body.rear||'factory')+', back glass '+(body.back||'factory')+(body.full?', windshield '+body.full:'')+(body.strip?', windshield strip':'');})
  .catch(function(x){clearInterval(tick);$('out').hidden=true;err.textContent=x.message})
  .finally(function(){btn.disabled=false;btn.textContent='Show My Tint'});};
})();
