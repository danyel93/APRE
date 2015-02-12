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
	/**************************************
	****Plugin AAQ| Crear Elementos en DOM
	**************************************/
	function Nuevo_ele(parametros){
		/*Contar los objetos: Object.keys(parametros).length
		  Nombre de la llave : key
		  Valor de la llave : parametros[llave];
		*/
	 	var new_div = document.createElement('div');
	 	var new_styl ="";
		for (var key in parametros) {
			if (key == "id" || key == "class") {
				new_div.setAttribute(key, parametros[key]);
			} else {
				new_styl += key+":"+parametros[key]+";"; 
				new_div.setAttribute("style", new_styl);
			}
			
		}
		return new_div;
	}
	/*************************************************
	/*************************************************
	***Plugin AAQ| Efecto Click Material Design*******
	**************************************************
	*************************************************/
	var e_boton = document.querySelectorAll(".boton");
	var Click_boton = function(evento){
		/*variables*/
		var xPantalla,yPantalla,xElemento,yElemento,xPos,yPos,top,left;
		var valores = this.getBoundingClientRect();
		console.log(evento);
		var contenedor_boton = this.target;
		yPos = evento.clientY-valores.top;
		xPos = evento.clientX-valores.left;
		//Dibujar
		var material_boton = new Nuevo_ele({
			"height":"1px",
			"width":"1px",
			"position":"absolute",
			"top":yPos+"px",
			"left":xPos+"px",
			"background-color":"#fff",
			"border-radius":"50%"
		});
		this.appendChild(material_boton);
		tamaño = (this.clientHeight*Math.PI)*2;
		margen = (this.clientHeight*Math.PI*2)/2;

		TweenMax.to(material_boton,0.8, {css: {
			opacity: "0",
			width:tamaño+"px",
			height:tamaño+"px",
			marginTop:"-"+margen+"px",
			marginLeft:"-"+margen+"px"
			},onComplete:Borrar_materialboton, ease: Power4.easeNone });

		function Borrar_materialboton(){
			var papi = this.target.offsetParent;
			papi.removeChild(this.target);
		}
		
	}

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

	
	/*CICLO PARA AÑADIR UN EVENTO CLICK*/
	for(var i=0;i<e_boton.length;i++){
		e_boton[i].addEventListener('click', Click_boton, false);
	}


	/*************************************************
	/*************************************************
	***JAVASCRIPT EFECTO ABOUT************************
	**************************************************
	*************************************************/
	/*Funcion*/
	// what should we do when scrolling occurs
	var item_scroll =  function(evt) {
	// Scroll de todo el body | Arreglado compatibilidad de firefox
	var body_scroll = document.documentElement.scrollTop||document.body.scrollTop;
		for (var i = 0; i < item.length; i++) {
			if (body_scroll>= (50+item[i].offsetTop) ){
				TweenMax.to(item[i],1, {css: {opacity: "1",marginTop:"0px"}, ease: Power4.easeNone });
			}
		}
	};
	/*Variables*/	
	var item = document.querySelectorAll(".acerca");
	item = Array.prototype.slice.call(item);
	//Funcion que escucha el scroll
	item.forEach(function(item) {
  		window.addEventListener("scroll", item_scroll);
	});
	item.forEach(function(item) {
  		window.addEventListener("load", item_scroll);
	});






	/*************************************************
	/*************************************************
	***JAVASCRIPT EFECTO MATERIAL DESING CIRCULAR*****
	**************************************************
	*************************************************/

	/******************
	 Variables Globales
	*******************/
	var contenedor_banco = document.getElementById('banco');
	///Variable con los elementos
	var ban_item = document.querySelectorAll(".mate-circ");
	///Variale del circulito
	var circulo = document.getElementById('circulito');
	var cir_estatus = "pintar";
	/*IMPORTANTE*/
	/*Asigno una variable temporal de identificacion cambiar con backend
	  y agregar un data-id con el id del proyecto.	
	*/
	for (var i = 0; i < ban_item.length; i++) {
		ban_item[i].setAttribute('data-idproyecto', 'idproyecto-'+i);
	}
	
	/*******************************************
	****Funcion Click En elementos  del Banco
	****Esta funcion es la principal
	*******************************************/
	var Click_ban_item = function(){
		/*variables*/
		var t_data = this.getAttribute("data-idproyecto");
		Ban_zindex(t_data);
		Dibujar_circulo(this,t_data);
	}
	/*CICLO PARA AÑADIR UN EVENTO CLICK*/
	for(var i=0;i<ban_item.length;i++){
		ban_item[i].addEventListener('click', Click_ban_item, false);
	}
	/***********************************
	****Funcion Agregar o Borrar Z-index
	************************************/
	function Ban_zindex(t_data){
		// Compruebo el estatus del circulo
		if (cir_estatus=="pintar") {
			for (var i = 0; i < ban_item.length; i++) {
				//Desabilito todos los click
				ban_item[i].style.pointerEvents = 'none';
				//Elemento Click
				if (ban_item[i].getAttribute("data-idproyecto") == t_data) {
					for (var x = 0; x < ban_item[i].childNodes.length; x++) {
						if (ban_item[i].childNodes[x].nodeName != "#text") {
							ban_item[i].childNodes[x].style.zIndex = "2";
							TweenMax.to(ban_item[i].childNodes[x], 0.6, {
								css: {
									color: "#ffffff"
								},
								ease: Power4.easeNone
							});
						}
					}
				}
				//Demas Click
				else {
					ban_item[i].style.zIndex = "3";
				}
			}
			cir_estatus = "borrar";
		}
		else if (cir_estatus == "borrar") {
			for (var i = 0; i < ban_item.length; i++) {
				ban_item[i].removeAttribute("style");
				//Elemento Click
				if (ban_item[i].getAttribute("data-idproyecto") == t_data) {
					for (var x = 0; x < ban_item[i].childNodes.length; x++) {
						if (ban_item[i].childNodes[x].nodeName != "#text") {
							ban_item[i].childNodes[x].removeAttribute("style");
						}
					}
				}
				//Demas Click
				else {
					ban_item[i].removeAttribute('style');
				}
			}
			cir_estatus="pintar"
		}
	}
	/***********************************
	****Funcion Dibujar Circulos
	************************************/
	function Dibujar_circulo(item,t_data){
		var x,y,dif_top = item.offsetTop,alto_item=item.clientHeight,dif_left = item.offsetLeft,ancho_item =item.clientWidth;
		var colores = ["#8BC34A","#FFC107","#2192D0","#3F51B5","#607D8B"];
		var col_random = colores[Math.floor(Math.random() * colores.length)];
		var elemento_padre = item.parentNode;
		var padre_ancho = elemento_padre.clientWidth,padre_alto = elemento_padre.clientHeight;
		y = dif_top+(alto_item/2)-(alto_item/2);
		x = dif_left+(ancho_item/2)-(alto_item/2);
		/*Propiedades del circulo*/
		var div_circulo = new Nuevo_ele({
			"id":"circulito",
			"class":"t-circulo",
			"height":alto_item+"px",
			"width":alto_item+"px",
			"background-Color":col_random,
			"top":y+"px",
			"left":x+"px",
		});
		elemento_padre.appendChild(div_circulo);
		
		//Guardo la animacion del circulo en una variable
		var cir = new TweenMax.to(div_circulo, 1, {css:{
			width:(padre_ancho*Math.PI)*2+"px",
			height:(padre_ancho*Math.PI)*2+"px",
			left:"-"+padre_ancho*3/Math.PI+"px",
			top:"-"+padre_ancho*3/Math.PI+"px",
		},delay:0.1,onReverseComplete:cir_func, ease:Quad.easeNone});
		//Play a la animacion
		cir.play();
		/// Funcion que dibuja la flecha
		Dibujar_regresar(elemento_padre,cir);
		/// Funcion despues del termino de la ani macion
		function cir_func(){
			var ani=this;
			TweenMax.to(this.target, 0.6, {css: {scale:0}, ease: Power4.easeNone});
			setTimeout(function(){ 
				Ban_zindex(t_data);
				elemento_padre.removeChild(ani.target)
			}, 300);
		}
		
	}
	/***************************************
	****Funcion Crear el elemento de regresar
	****************************************/
	function Dibujar_regresar(elemento_padre,cir){
		var flecha_regresar = new Nuevo_ele({
			"id":"flecha",
			"class":"flecha",
		});
		flecha_regresar.innerHTML='<i aria-hidden="true" class="icon-cerrar"></i>';
		contenedor_banco.appendChild(flecha_regresar);
		 /*Se agrega un evento de escuchar click al boton de la flecha*/
		flecha_regresar.addEventListener('click', function (){
			var efecto_flecha = new Nuevo_ele({
				"height":"40px",
				"width":"40px",
				"top":"50%",
				"left":"50%",
				"margin-left":"-20px",
				"margin-top":"-20px",
				"position":"absolute",
				"background-color":"#fff",
				"border-radius":"50%"
			});
			this.appendChild(efecto_flecha);
			TweenMax.to(efecto_flecha, 0.6, {css: {scale:3,opacity:0}, ease: Power4.easeNone});
			///Funcion para revertir el circulo
			cir.reverse()			
		}, false);//evento click
		
	}
	
})();