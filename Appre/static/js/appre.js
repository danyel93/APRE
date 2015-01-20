//Variable inicial
var cabezal = $('header');
var h_menu =$('.nav-icon');
// Opacidad para el header (100% Funcional)	
$(window).bind('scroll', function(){
	var color = "#00897B";
	
	// Variables  
   	
   	var op_start=1 // 2px de scroll o menos quivale a 1 de opacidad
   	var op_end= 600 // 600px  de de scroll o mas equivale a 0.3 de opacidad
	//Variables
	var po_scroll = $(window).scrollTop();
	var opacity = 1;
	//console.log("la posicion actual es:"+po_scroll+", y la opacity es = "+opacity);
	if (po_scroll <= op_start) {
		opacity = 0;
	} else if (po_scroll <= op_end) {
		opacity =  po_scroll / op_end;
	}

	console.log(opacity);
	var rgbaCol = 'rgba(' + parseInt(color.slice(-6,-4),16)
    + ',' + parseInt(color.slice(-4,-2),16)
    + ',' + parseInt(color.slice(-2),16)
    +','+opacity+')';
	cabezal.css({
		'background-color': rgbaCol,
	});
});
