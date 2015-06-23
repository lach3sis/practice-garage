$(document).on('ready', function(){
    
	    	/*
		 * add contact event listener
		 */
		$('.idothisthing').on('click', '#save_contact_to_car', function(e){
			e.preventDefault();
			carkey = $(this).attr('carid');
			var contact = {};
			contact.name = $('#contact_first_name').val();
			contact.email = $('#contact_email').val();
			contact.tel_nr = $('#contact_tel').val();
			contact.klootfactor = $('#contact_klootfactor').val();
			contact.gender = $('#contact_gender').val();
			contact.car = carkey;
			sendcontact(contact);
		});
		
		load_garages();
	    __init__();
	    
	    
    
    
    });
    
    function load_garages(){
    $container = $('#row1_container');
		var urllink = '/get_garages';
		$.ajax({
			url: urllink,
			cache: false,
			async: true,
			type: "GET",
			success: function(html){
				console.log(html);
				
				$container.append(html);
				__init__();
			}
		});
    }
    function __init__()
    {
    
    	
	   	$('.idothisthing').on('click', '#recalc_btn', function()
		{	
			var sid = $(this).attr('sid');
			console.log(sid);	
			get_service_cost(sid);
		});
	
    	$('#content-row1').on('click', '#disp_car_page_btn', function(e) 
    	{
			ident = $(this).attr("cid");
			current_car ={};
			current_car.ident = ident;
			load_the_bloodclat_car_thingy(ident);
		});
	    		
    		$('.row1').contenthover({
    		effect:'slide',
    		slide_speed:300,
    		overlay_background:'#000',
    		overlay_opacity:0.6
			});

    		
			//----------------//
			$('.row2').contenthover({
    		effect:'fade',
    		slide_speed:300,
    		overlay_background:'#000',
    		overlay_opacity:0.6
			});


			$('.row3').contenthover({
    		effect:'slide',
    		slide_direction: 'top',
    		slide_speed:300,
    		overlay_background:'#000',
    		overlay_opacity:0.6
			});
			
		$('#avatar_btn').on('click', function(){
			
			$container = $('div#content-row1');
			$modal = $('div#uploadPic_modal');
			var ident = $(this).attr('car_id');
			var urllink = '/load_add_carimg_modal/'+ident;
			

			
			if(typeof got_data !== 'undefined')
			{
			
				$('#uploadPic_modal').modal();
				
			}else{
			
				$.ajax({
					url: urllink,
					type: 'GET',
					cache: false,
					async: true,
					success: function(html)
					{
						$modal.append(html);	
						$('#uploadPic_modal').modal();
						got_data = true;
					}
				});
			}
			
		});
		
		
		$('.show_car_btn').on('click', function()
		{
   		
   			ident = $(this).attr('garage_id');
   			fade_row1();
   			$.ajax({
    			url : '/car/'+ident,
    			type: 'GET',
    			cache: false,
    			async: true,
    			success: function(html)
    			{
   				
    				$('#content-row1').fadeIn(50);
    				$('#content-row1').html(html);
    				
    				$tstring = '';
    				
    				$tstring += '<div id="car_form" class="form">';
					$tstring += '<div class="form-group">';
					$tstring += '<h3> New Car </h3>';
					$tstring += 'Car name:  <input type="text" id="car_name" name="car_name"/>'; 
					$tstring += 'Car brand: <input id="car_brand" name="car_brand" />';
					$tstring += '</div>';	
					$tstring += '<div class="form-group">';
					$tstring += '<button garage_id="'+ident+'" id="save_car_btn" class="btncarsave">save car</button>';
					$tstring += '</div>';
					$tstring += '</div>';
    				
    				$('#content-row1').prepend($tstring);
    				__init__();	
   				}
   			});
   		});
   		
   		
	}
	
			
	$('#content-row1').on('click', '.btncarsave', function(e)
	{
		e.preventDefault();
		key = $(this).attr("garage_id");
		console.log('Garage ident :' +key);
		
		var c = {};
  		c.garage = key;
  		c.brand =  $('#car_brand').val();
  		c.name = $('#car_name').val();
  		
  		console.log(c.name);
		console.log(c);
		sendcar(c);
	});
	
	
	$('#row1_container').on('click', 'button.get_garage_avatarForm', function(){
	
		ident = $(this).attr('garage_id');
		$container = $('#content-row1');
		var urllink = '/upload_garage_avatar/'+ident;
		$.ajax({
			type: "GET",
			url: urllink,
			cache: false,
			async: false,
			success: function(html){
				
				$container.fadeIn();
				$container.html(html);
			
			}
		});

	});
	
	function fade_row1()
	{
		
		$('#content-row1').fadeOut();

	}
	
	
	function sendcar(params){
		$.ajax({
			type: "POST",
			url: "/cars",
			data: params,
			success: function(){
				alert('car added');			
				getcars(params.garage);
			}
		});
	}
	
	
	//Request a list of all current cars and append them to div.garagelijst
	function getcars(garage)
	{	
		console.log(garage);
		$.ajax({
			url: "/car/"+garage,		
			type: "GET",
			success: function(html){
				
				$('#content-row1').html(html);
				
				$tstring = '';
   				
   				$tstring += '<div id="car_form" class="form">';
				$tstring += '<div class="form-group">';
				$tstring += '<h3> New Car </h3>';
				$tstring += 'Car name:  <input type="text" id="car_name" name="car_name"/>'; 
				$tstring += 'Car brand: <input id="car_brand" name="car_brand" />';
				$tstring += '</div>';	
				$tstring += '<div class="form-group">';
				$tstring += '<button garage_id="'+garage+'" id="save_car_btn" class="btncarsave">save car</button>';
				$tstring += '</div>';
				$tstring += '</div>';
   				
   				$('#content-row1').prepend($tstring);
   				
   				__init__();	
   				
			}
		});
	}
	
function get_service_form(carkey)
{
	$.ajax({
		type: "GET",
		url: "/add_service/"+carkey,
		async: true,
		cache: false,
		processData: true,
		success: function(data)
		{
			console.log(data);
		}
	}).done(function( data ) {
		$( "#contact-holder" ).html("");
		$(	"#contact-holder").html("<h2>Add A Service</h2>");
	    $( "#contact-holder" ).append( data );
	   
	    //add_service_click_listener();
		
	  });
}

function add_service(service)
{
	var url = "/add_service/"+service;
	$.ajax({
		url: url,
		type: "POST",
		data:  service,
		processData: true,
		cache: false,
		success: function(data){
			
			console.log(data);
		}
	});
}

	//load the car profile page thingy
	function load_the_bloodclat_car_thingy(ident){
	var url = "/carprofile/"+ident;
	$.ajax({
		type: "GET",
		url: url,
		success: function(data){
			$('.idothisthing').html(data);
			getcontactbycar(ident);
			//load_car_avatar($('div#garage-list #current_carkey').val());
		}
	});
}


function getcontactbycar(ident){
	console.log("loading contact");
	var url = "/contacts/"+ident;
	$.ajax({
		type: "GET",
		url: url,
		success: function(html){
			$('#contact-holder').html(html);
			
		}
	});
}

/*
*
* New Contact
*/
function sendcontact(params){
	$.ajax({
		type: "POST",
		url: "/contacts",
		data: params,
		cache: false,
		success: function(data)
		{
			getcontactbycar(params.car);
			var car_id = params.car;
			var email = params.email;
			var gender = params.gender;
			var klootfactor = params.klootfactor;
			var name = params.name;
			var tel_nr = params.tel_nr;
			$('#_contact-name').text(name);
			$('#_contact-email').text(email);
			$('#_contact-gender').text(gender);
			$('#_contact-klootfactor').text(klootfactor);
			$('#_contact-telephone').text(tel_nr);	
		}
	});
}	


$('.idothisthing').on('click', '#addcontact_btn', function(){
		
		$('#contactform').fadeIn();
	});	
	
	
	$('.idothisthing').on('click', '#btn_getcontactfrm', function()
	{	
		var ident = $(this).attr('carid');
		$container = $('div#modal-content');
		if(ident !== "" || ident !== null)
		{
			var urllink = '/addcontact_to_car/'+ident;
			$.ajax({
				type: 'GET',
				url: urllink,
				cache: false,
				async: false,
				success: function(html)
				{
					$container.html(html);
					console.log(html);
					$('div#kanker').modal('show');
				}
			});
		}
	});
	
	
	$('#kanker').on('click', '#save_contact_to_car', function(){
	
		carkey = $(this).attr('carid');contact = {}
		
		contact.name = $('#input_first_name').val();
		contact.email = $('#input_email').val();
		contact.tel_nr = $('#input_tel').val();
		contact.klootfactor = $('#contact_klootfactor').val();
		contact.car = carkey;
		contact.gender = $('#contact_gender').val();
		console.log(contact);
		sendcontact(contact);
		
		
	});
	
	$('.idothisthing').on('click', '#add_service_btn', function(e){
		e.preventDefault();
		console.log('kankerzooi');
		carkey = $(this).attr("carid");  		
		get_service_form(carkey);
		add_service_click_listener();
	});
	
		$('.idothisthing').on('click', '#list_services', function()
	{	
		//console.log( $(this).attr('carid') );
		//$('#content-holder-1').html("");
		show_service_list();	
	});
	
	
	function add_service_click_listener(){

		$('.idothisthing').on('click', '#save_service', function(e){
			e.preventDefault();
			var service = {};
			service.replacement_part = $('#replacement_part').val();
			service.price_part = $('#price_part').val();
			service.worked_hrs = $('#worked_hrs').val();
			service.carid = $('#save_service').attr('carid');
			
			add_service(service);
			return false;
			
		});
	}
	
function show_service_list()
{
	
	car_id = $('#list_services').attr('carid');
	url = "/services/"+car_id;
	$.ajax({
		url: url,
		async: true,
		cache: false,
		success: function(html)
		{
			$('#service_list').html("");
			$('#service_list').html(html);
			var price = $('#content-holder-1 div#_service_price').attr('service_pricepart');
			var hours_worked = $('#content-holder-1 div#_service_worked_hrs').attr('service_worked_hrs');
			var garage_price_per_hour = $('#garage_price').attr('price_per_hour');
			var service_cost = ( price + ( hours_worked * garage_price_per_hour ) );
			$('div#_service_total').html('');
			$('div#_service_total').html(''+service_cost);
		}
	});
}


	
function get_service_cost(sid)
{
	if(sid !== "" || sid !== null){
		carkey = $('#car_ident').attr('ident');
		urllink = "/services/";
		$.ajax({
			url: urllink,
			data: { "carkey": carkey,
					"topic": "get_servicecosts",
					"ident" : sid
					},
			async: true,
			cache: false,
			processData: true,
			type: "GET",
			success: function(data)
			{
				console.log($('#service_'+sid+ ' input.text').attr('id'));
				$('#service_'+sid+ ' input#_service_total_'+sid).val('');
				$('#service_'+sid+ ' input#_service_total_'+sid).val('total :'+data);
			}
		});
	}
}