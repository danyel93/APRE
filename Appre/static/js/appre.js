//Variable inicial
var cabezal = $('header');
var h_menu =$('.nav-icon');
// Opacidad para el header (100% Funcional)	
$(window).bind('scroll load ', function(){
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

	var rgbaCol = 'rgba(' + parseInt(color.slice(-6,-4),16)
    + ',' + parseInt(color.slice(-4,-2),16)
    + ',' + parseInt(color.slice(-2),16)
    +','+opacity+')';
	cabezal.css({
		'background-color': rgbaCol,
	});
})
;(function() {
	/*Inicializar LazyLoad*/
	var bLazy = new Blazy({
		offset: 100,
		success: function(element,msg){
		    
			Borrar_cargando(element,msg);
	    },
	    error: function(ele, msg){
	    	/*Realizo una sobrecarga a la imagen*/
            if(msg === 'missing'){
				Borrar_cargando(ele,msg);	
            }
            else if(msg === 'invalid'){
       
				Borrar_cargando(ele,msg);	
            }
        } 
    });
    function Borrar_cargando(elemento, msg) {
		/*Quitar Elemento*/
		/*Selecciono el elemento padre*/
		var figure = elemento.parentNode;
		if (elemento==undefined){
			console.log("indefinido")
		}
		/*comprobacion si existe circulo*/
		var circulo = "";
		/*Busco el elemento cir-car y lo elimino*/
		for (var i = 0; i < figure.childNodes.length; i++) {
			if (figure.childNodes[i].className == "cir-car") {
				circulo = figure.childNodes[i];
				break;
			}
		}
		if (circulo == null){
			figure.removeChild(circulo);
		}
		
		TweenMax.to(elemento, 1, {css: {opacity: "1"}, ease: Power4.easeNone }); 
	}/*Fin borrar cargando*/

	/**
	 * Efecto Circular
	 **/
	///Variable con los elementos
	var ban_item = document.querySelectorAll(".mate-circ");
	///Variale del circulito
	var circulo = document.getElementById('circulito');
	/*Asigno una variable temporal de identificacion cambiar con backend*/
	for (var i = 0; i < ban_item.length; i++) {
		ban_item[i].setAttribute('data-idproyecto', 'idproyecto-'+i);
	}
	/*Funcion Click en BANCO DE PROYECTOS*/
	var Click_ban_item = function(){
		/*variables*/
		var t_data = this.getAttribute("data-idproyecto");
		Ban_zindex(t_data);
		Dibujar_circulo(this);
	}
	/*Funcion Add click*/
	for(var i=0;i<ban_item.length;i++){
		ban_item[i].addEventListener('click', Click_ban_item, false);
	}
	/*Funcion Agregar Z-index*/
	function Ban_zindex(t_data){
		for (var i = 0; i < ban_item.length; i++) {
			//Elemento Click
			if (ban_item[i].getAttribute("data-idproyecto")==t_data){
				console.log("seleccione "+ban_item[i].getAttribute("data-idproyecto"));
				for (var x = 0; x < ban_item[i].childNodes.length; x++) {
					if (ban_item[i].childNodes[x].nodeName !="#text"){
						ban_item[i].childNodes[x].style.zIndex="2";
						TweenMax.to(ban_item[i].childNodes[x], 0.6, {css: {color: "#ffffff"}, ease: Power4.easeNone });
					}
				}
			}
			//Demas Click
			else{
				console.log("no seleccione "+ban_item[i].getAttribute("data-idproyecto"))
				ban_item[i].style.zIndex="3"
			}
		}
	}
	function Dibujar_circulo(item){
		var x,y,dif_top = item.offsetTop,alto_item=item.clientHeight,dif_left = item.offsetLeft,ancho_item =item.clientWidth;
		var colores = ["#8BC34A","#795548","#FFC107","#2192D0","#3F51B5","#607D8B"];
		var col_random = colores[Math.floor(Math.random() * colores.length)];
		var elemento_padre = item.parentNode;
		var padre_ancho = elemento_padre.clientWidth,padre_alto = elemento_padre.clientHeight;
		var div_circulo = document.createElement('div');
		y = dif_top+(alto_item/2)-(alto_item/2);
		x = dif_left+(ancho_item/2)-(alto_item/2);
		/*Propiedades del circulo*/
		div_circulo.id = "circulito";
		div_circulo.className = "t-circulo"
		div_circulo.style.height=alto_item+"px";
		div_circulo.style.width=alto_item+"px";
		div_circulo.style.backgroundColor=col_random;
		div_circulo.style.top=y+"px";
		div_circulo.style.left=x+"px";
		elemento_padre.appendChild(div_circulo);
		TweenMax.to(div_circulo, 1, {css:{
			width:(padre_ancho*Math.PI)*2+"px",
			height:(padre_ancho*Math.PI)*2+"px",
			left:"-"+padre_ancho*3/Math.PI+"px",
			top:"-"+padre_ancho*3/Math.PI+"px"
		},delay:0.1, ease:Quad.easeNone});

	}
})();