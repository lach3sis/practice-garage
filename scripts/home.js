// define globals used in the file
/* globals _base_ */

// initiate a name space (before using it)
var __garage__ = {};
var garEdit = {};

function init(){
	
	
/* =======================Garage Buttons===================*/
		
		
//	Button Insert new Garage is clicked	
	$('#add-garage').on('click', function() {
		var d = {};
		d.name = $('#g-name').val();
		d.brand =  $('#g-brand').val();
		d.note = $('#note').val();
		d.postal_country = $('#postal_country').val();
		d.price_per_hours = $('#price_per_hours').val();
		if (document.getElementById('roundup_workhrs').checked){
			d.round_up_workhrs = true;
		}else{
			d.round_up_workhrs = false;
		}
		send(d);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
		console.log(d);
		__garage__.load();
	});	
	
	
	//Button Edit garage is clicked 
	$('#garagelijst').on('click', '.btnedit', function(){
		key = $(this).attr("garage_id");
		current_garage ={};
		current_garage.key = key;
		console.log(current_garage.key);
		show(current_garage);
	});
	
	
	//Button show garage profile is clicked 
	$('#garagelijst').on('click', '#garage_', function(){
		key = $(this).attr("gid");
		current_garage ={};
		current_garage.key = key;
		console.log(current_garage.key);
		show_g_temp(current_garage.key);
	});
	
	
	//Button get garage  is clicked 
	$('#garagelijst').on('click', '#get_garage_btn', function(){
		key = $(this).attr("gid");
		current_garage ={};
		current_garage.key = key;
		console.log(current_garage.key);
		show_g_temp(current_garage.key);

	});
	
	
	//Button get garage  is clicked 
	$('#garagelijst').on('click', '#avatar_btn', function(){
		console.log("test");
		key = $(this).attr("car_id");
		car ={};
		car.key = key;
		console.log(car.key);
		upload_avatar(car.key);

	});
	
	
	//Save Garage edit button is clicked  Done button is clicked
	//#wrapper edited 
	$('#editlist').on('click', '.save', function(){
		var garEdit = {};
		garEdit.key = $(this).attr("garage-id");
		garEdit.name = $('#editname').val();
		garEdit.brand = $('#editbrand').val();
		garEdit.note = $('#editnote').val();
		garEdit.postal_country = $('#editpostal_country').val();
		garEdit.price_per_hour = $('#editpph').val(); 
		garEdit.round_up_workhrs= $('#editroundup').val();
		console.log("editing Now!");
		edit(garEdit);
	});
	
	
	//button.btn3 is clicked Delete
	$('#cont').on('click', '.btn3', function(){
		key = $(this).attr("garage_id");
		key2 = {};
		key2.gid = key;
		del(key2);
	});
	
	
	//button.btn3 is clicked Delete
	$('#garagelijst').on('click', '.btndel', function(){
		key = $(this).attr("garage_id");
		key2 = {};
		key2.gid = key;
		del(key2);
	});
	
	
	$('#garagelijst').on('click', '#addcontact_btn', function(){
		$('#contactform').fadeIn();
	});
	
	
	//Button press me
	$('#garagelijst').on('click', '.btntest', function(e) {
		console.log("test");
		key = $(this).attr("garage_id");
		current_garage ={};
		current_garage.key = key;
		load_garage_page(key);	
	});
	
	
	$('#garagelijst').on('click', '#disp_car_page_btn', function(e) {
		console.log("test");
		ident = $(this).attr("cid");
		current_car ={};
		current_car.ident = ident;
		load_car_page(ident);
	});
	
	
	//Button press me
	$('.user-menu-list').on('click', '#view_car_btn', function(e) {
		e.preventDefault();
		console.log("Loading Cars!");
		key = $(this).attr("garage_id");
		current_garage ={};
		current_garage.key = key;
		console.log("Got Cars from:");
		getcars(key);
	});
	
	/* =======================END Garage Buttons===================*/		
	
	
	/* =======================Car Buttons===================*/
	//save car
	$('#garagelijst').on('click', '.btncarsave', function(e){
		e.preventDefault();
		key = $(this).attr("garage_id");
		console.log(key);
		var c = {};
  		c.garage = key;
  		c.brand =  $('#car_brand').val();
  		c.name = $('#car_name').val();
  		console.log(c.name);
		console.log(c);
		sendcar(c);
	});
	
	/*
	 * add contact event listener
	 */
	$('#garagelijst').on('click', '#save_contact', function(e){
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
	
	
	//delete car
	$('#garagelijst').on('click', '.del_car_btn', function(){
		console.log("Geklikt op knop Del");
		key = $(this).attr("car_id");
		key2 = {};
		key2.gid = key;
		delete_car(key2);
		getpage();
	});
		
	
	$('#garagelijst').on('click', '#testthis', function(){
		console.log("Geklikt");
		var car = {};
		car.id = $(this).attr("car_id");
		car.name = $('#editcar_name_'+car.id).val();
		car.brand = $('#editcar_brand_'+car.id).val();
		car.garage = $(this).attr("garage_id");
		console.log(car);
		editcar(car);
	});
	
	
	add_service_click_listener();
	$('#garagelijst').on('click', '#addcontact_btn', function(){
		
		$('#contactform').fadeIn();
	});
		
	
	$('#garagelijst').on('click', '#close_btn', function(){
		getcars($(this).attr("garage_id"));
	});
			
		
	//Button refresh cars is clicked
	$('#cont').on('click', '.refresh-cars', function(e) {
		console.log("test");
		var cars_list = $(this).attr('cars-list');
		$.ajax({
			url: "/garage/" + $(this).closest('.refresh-cars').attr('ident') + '/cars',
			type: "GET",
			success: function(data){
				getcars();
			}
		});
	});
	
	$('#add_garage_btn').on('click', function()
	{
		
		load_add_garage_form();
	});
	
	
	
	
	$('#garagelijst').on('click', '#recalc_btn', function()
	{	
		var sid = $(this).attr('sid');	
		get_service_cost(sid);
	});
	
	
	//Save new Service to car
	$('#garagelijst').on('click', '#add_service_btn', function(e){
		e.preventDefault();
		carkey = $(this).attr("carid");  		
		get_service_form(carkey);
	});
	
	
	$('#garagelijst').on('click', '#list_services', function()
	{	
		console.log("fuck yeah");
		$('#content-holder-1').html("");
		show_service_list();	
	});
	
		/* =======================END Car Buttons===================*/
		
	//Refresh me button is clicked
		$('#refresh').on('click', function(){
			getpage();
		});

	// controleren <<<<<<<<<<<<<<<	
	//Add New Car
//		$('#garagelijst').on('click', '.btnadd', function(){
//			/*jshint multistr: true */
//			var carform = " <div id='carinput' style='margin-left:1px; margin-top:5px; margin-bottom:10px; padding: 2px,2px,2px,2p'> \
//							<form> \
//								<span style='text-align:center; color:blue' > New Car</span><br> \
//								<ul style='left:0px'> \
//							    <li>Car name:  <input type='text' id='car_name' name='car_name'/></li><br> \
//							    <li>Car brand: <input id='car_brand' name='car_brand' /> </li> \
//							    </ul> \
//						   </form>\
//						   <button garage_id='" + $(this).attr('garage_id') + "' garage_name='"+ $(this).attr('garage_name') +"' class='btncarsave' style='margin-left: 15px' >save car</button> \
//						   </div>";
//			
//			console.log("ADDING");
//			garage = $(this).attr("garage_id");
//			garage_name = $(this).attr("garage_name");
//			current_car = {};
//			current_car.gid = garage;
//			current_car.gname = garage_name;
//			//Append a small input field to the garages div klopt niet meer
//			$('#cont').append(carform);
//		});
//}
}

// standard function example, needs to be defined before used!
function load() {
	/**
	 * execute load for dynamic content
	 */
	// function can be plain or called inside a namespace
	__garage__.load();
}


$(function() {
	/****
	 * $(function() <code>)}
	 * contains code that will be executed when page is loaded
	 */	
	init();
	load();

});


// namespace can contain functions (i prefer to use namespaces)
__garage__.load = function(){
	/**
	 * Loads the list garages
	 */
	_base_.log("loading garages");
	$.ajax({type: "GET", url:"/garages", success: function(data) {
		$('#garage-list').html(data);
		
	}});
};


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


function delete_car(key){
	var url = "/car/"+key.gid;
	console.log('URL: ' + url);
	$.ajax({
		type: "DELETE",
		url: url,
		data: key,
		success: function (){
			getcars(key.garagekey);
		}
	});
}


//Request a list of all current cars and append them to div.garagelijst
function getcars(garage){	
	console.log(garage);
	$.ajax({
		url: "/car/"+garage,		
		type: "GET",
		success: function(data){
			$('#car-list').html(data);
		}
	});
}


//Called by button.send Request a Save for new garage to datastore
function send(params){
	alert(params);
	$.ajax({
		type: "POST",
		url: "/garages",
		data: params,
		success: function(){		
//				$('#garage-list').html(params);
				getpage();
		}
	});
}


//Function called by button.eddit show garage to edit
function show(g){
	var url = "/garages/"+g.key;
	$.ajax({
		type: "GET",
		url: url,
		data: g,
		success: function(data){
			$('#editlist').html(data);
		}
	});
}


//Function called by button.eddit show garage to edit
function show_g_temp(g){
	alert("here we go !");
	var url = "/showgarage/"+g;
	$.ajax({
		type: "GET",
		url: url,
		data: g,
		success: function(data){
			$('#page-container').html(data);
		}
	});
}


function upload_avatar(ident){
	var url = "/upload_avatar/"+ident;
	$.ajax({
		type: "GET",
		url: url,
		success: function(data){
			$('#garagelijst').html(data);
		}
	});
}


//Function called press me
function load_garage_page(garage){
	var url = "/editgarage/"+garage;
	console.log('URL:' +url);
	console.log(garage);
	$.ajax({
		type: "GET",
		url: url,
		data: garage.key,
		success: function(data){
			$('#editlist').html(data);
			getcars(current_garage.key);
			
		}
	});
}


function load_car_page(ident){
	var url = "/carprofile/"+ident;
	$.ajax({
		type: "GET",
		url: url,
		success: function(data){
			$('#garage-list').html(data);
			getcontactbycar(ident);
			load_car_avatar($('div#garage-list #current_carkey').val());
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


//Function Called by button.save  Garage is edited. request save to datastore
function edit(params){
	console.log(params);
	$.ajax({
		type: "PUT",
		url: "/garage/"+params.key,
		data: params,
		success: function(){
			load();
		}
	});	
}


function editcar(params){
	console.log(params);
	$.ajax({
		type: "PUT",
		url: "/car/"+params,
		data: params,
		success: function(){
		}
	});	
}


function del(key){
	alert("home" + key.gid);
	var url = "/garage/"+key.gid;
	console.log('URL: ' + url);
	alert('URL: '+ url );
	$.ajax({
		type: "DELETE",
		url: url,
		data: key,
		success: function (){
			getpage();
		}
	});
}


function getpage(){
	$.ajax({
		url: "/garage",
		type: "GET",
		success: function(data){
			$('#garage-list').html(data);
			
		}
	});
}

//function load_car_avatar(car_key){
//	
//	var urllink = '/view_photo/'+car_key;
//	$.ajax({
//		url : urllink,
//		type: "GET",
//		cache: false,
//		async: true,
//		success: function(data){
//			console.log('got data');
////			$('#testme').html('');
////			$('#testme').append(data);
//			
//		}
//	});
//}

//function sendcar(params){
//	$.ajax({
//		type: "POST",
//		url: "/car",
//		data: params,
//		success: function(){
//			alert('car added');			
//			console.log(params);
////			getcars();
//		}
//	});
//}


function get_service_form(carkey){
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
		$( "#contact-holder .panel-body" ).html("");
		$(	"#contact-holder .panel-heading").html("<h2>Add A Service</h2>");
	    $( "#contact-holder .panel-body" ).html( data );
	   
	    add_service_click_listener();
		
	  });
}


function add_service_click_listener(){
	
	
	$('#add_service_template').on('click', '#save_service', function(e){
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


function add_service(service){
	var url = "/add_service/"+service;
	$.ajax({
		url: url,
		type: "POST",
		data:  service,
		processData: true,
		cache: false,
		success: function(data){
			
		}
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
			$('div#garage-form-container').fadeOut();
			$('#contact-holder').html(html);
			var price = $('#content-holder-1 div#_service_price').attr('service_pricepart');
			var hours_worked = $('#content-holder-1 div#_service_worked_hrs').attr('service_worked_hrs');
			var garage_price_per_hour = $('#garage_price').attr('price_per_hour');
			var service_cost = (price + (hours_worked * garage_price_per_hour));
			$('div#_service_total').html('');
			$('div#_service_total').html(''+service_cost);
		}
	});
}

function load_add_garage_form()
{
	var urllink = '/add_garage';
	$container  = $('div#gar-form-holder');
	$flushit = $('div#garagelijst');
	
	$.ajax({
		type: "GET",
		url: urllink,
		cache: false,
		async:false,
		success: function(html)
		{
			$container.fadeOut();
			$container.fadeIn();
			$flushit.fadeOut();
			$container.html(html);
			init();
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