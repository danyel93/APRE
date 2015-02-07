// Avoid `console` errors in browsers that lack a console.
(function() {
    var method;
    var noop = function () {};
    var methods = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeStamp', 'trace', 'warn'
    ];
    var length = methods.length;
    var console = (window.console = window.console || {});

    while (length--) {
        method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
            console[method] = noop;
        }
    }
}());


/*!
  hey, [be]Lazy.js - v1.3.1 - 2015.02.01
  A lazy loading and multi-serving image script
  (c) Bjoern Klinggaard - @bklinggaard - http://dinbror.dk/blazy
*/
  ;(function(d,h){"function"===typeof define&&define.amd?define(h):"object"===typeof exports?module.exports=h():d.Blazy=h()})(this,function(){function d(b){if(!document.querySelectorAll){var g=document.createStyleSheet();document.querySelectorAll=function(b,a,e,d,f){f=document.all;a=[];b=b.replace(/\[for\b/gi,"[htmlFor").split(",");for(e=b.length;e--;){g.addRule(b[e],"k:v");for(d=f.length;d--;)f[d].currentStyle.k&&a.push(f[d]);g.removeRule(0)}return a}}m=!0;k=[];e={};a=b||{};a.error=a.error||!1;a.offset=a.offset||100;a.success=a.success||!1;a.selector=a.selector||".b-lazy";a.separator=a.separator||"|";a.container=a.container?document.querySelectorAll(a.container):!1;a.errorClass=a.errorClass||"b-error";a.breakpoints=a.breakpoints||!1;a.successClass=a.successClass||"b-loaded";a.src=r=a.src||"data-src";u=1<window.devicePixelRatio;e.top=0-a.offset;e.left=0-a.offset;f=v(w,25);t=v(x,50);x();n(a.breakpoints,function(b){if(b.width>=window.screen.width)return r=b.src,!1});h()}function h(){y(a.selector);m&&(m=!1,a.container&&n(a.container,function(b){p(b,"scroll",f)}),p(window,"resize",t),p(window,"resize",f),p(window,"scroll",f));w()}function w(){for(var b=0;b<l;b++){var g=k[b],c=g.getBoundingClientRect();if(c.right>=e.left&&c.bottom>=e.top&&c.left<=e.right&&c.top<=e.bottom||-1!==(" "+g.className+" ").indexOf(" "+a.successClass+" "))d.prototype.load(g),k.splice(b,1),l--,b--}0===l&&d.prototype.destroy()}function z(b,g){if(g||0<b.offsetWidth&&0<b.offsetHeight){var c=b.getAttribute(r)||b.getAttribute(a.src);if(c){var c=c.split(a.separator),d=c[u&&1<c.length?1:0],c=new Image;n(a.breakpoints,function(a){b.removeAttribute(a.src)});b.removeAttribute(a.src);c.onerror=function(){a.error&&a.error(b,"invalid");b.className=b.className+" "+a.errorClass};c.onload=function(){"img"===b.nodeName.toLowerCase()?b.src=d:b.style.backgroundImage='url("'+d+'")';b.className=b.className+" "+a.successClass;a.success&&a.success(b)};c.src=d}else a.error&&a.error(b,"missing"),b.className=b.className+" "+a.errorClass}}function y(b){b=document.querySelectorAll(b);for(var a=l=b.length;a--;k.unshift(b[a]));}function x(){e.bottom=(window.innerHeight||document.documentElement.clientHeight)+a.offset;e.right=(window.innerWidth||document.documentElement.clientWidth)+a.offset}function p(b,a,c){b.attachEvent?b.attachEvent&&b.attachEvent("on"+a,c):b.addEventListener(a,c,!1)}function q(b,a,c){b.detachEvent?b.detachEvent&&b.detachEvent("on"+a,c):b.removeEventListener(a,c,!1)}function n(a,d){if(a&&d)for(var c=a.length,e=0;e<c&&!1!==d(a[e],e);e++);}function v(a,d){var c=0;return function(){var e=+new Date;e-c<d||(c=e,a.apply(k,arguments))}}var r,a,e,k,l,u,m,f,t;d.prototype.revalidate=function(){h()};d.prototype.load=function(b,d){-1===(" "+b.className+" ").indexOf(" "+a.successClass+" ")&&z(b,d)};d.prototype.destroy=function(){a.container&&n(a.container,function(a){q(a,"scroll",f)});q(window,"scroll",f);q(window,"resize",f);q(window,"resize",t);l=0;k.length=0;m=!0};return d});