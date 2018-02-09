$(document).ready(function() {
	/*when enter is clicked for the budget form send them to next form instead of submitting entire form */
	/*should do some error handling but too lazy*/
	$(document).on("keypress", "#questionCarousel", function(event) {
		if (event.keyCode == 13) {
			if ($("#phoneBudgetQ").is(":visible")) {
				event.preventDefault();
				$(".next-button.btn.btn-success").trigger('click');
			};
		};
	});
	
	/*keep buttons highlighted if they were previously checked*/
	$(".btn.btn-primary").each(function() {
		/*needs to be opposite of below */
		var checked = ($(this).next().is(':checked'));
		/*this determines which of two color options are chosen for the button depending on checked */
		var color = checked ? '#42c8f4' : '#337ab7';
		/*change the color of the button once clicked */
		$(this).css('background-color', color);
	});		
	
	/*highlight preference button when checked */
	$(document).on("click",".btn.btn-primary", function(){
		/*need to use opposite value as when I first click it will see as not checked */
		var checked = !($(this).next().is(':checked'));
		/*this determines which of two color options are chosen for the button depending on checked */
		var color = checked ? '#42c8f4' : '#337ab7';
		/*change the color of the button once clicked */
		$(this).css('background-color', color);
	});
	
	/*initialize the tooltip*/
	$('[data-toggle="tooltip"]').tooltip();
	
	/*check if row clicked */
	$(document).on("click","#resultsTable tr", function() {		
		/*if row clicked is not selected AND is not the table header row...*/
		if (!($(this).hasClass("rowSelected")) && !($(this).parent().is("thead"))) {
			
			/*once you click on a row the tooltip is destroyed
			 * therefore, we check whether row selected is not the first one as that
			 * will be clicked at the beginning */
			if ($(this).prev("tr").length == 1) {
				$('[data-toggle="tooltip"]').tooltip("disable");
			}
			
			/*add highlight formatting to clicked row and remove children in pros/cons containers*/
			$(this).addClass("rowSelected");
			var compContainers = $(this).find(".compContainer");
			compContainers.first().empty();
			compContainers.last().empty();
		
			/*get the ranked phones with data from html file and parse it into a json array*/
			rankedPhones = JSON.parse($("#rankedPhones_json").val());
			/*get id of clicked row and then get the corresponding rankedPhone variable*/
			var indexSelected = $(this).children('th').first().html();
			var selectedPhone = rankedPhones[indexSelected-1];
								
			/*remove the highlight formatting from any other row and add the pros/cons*/
			/*added the filter by "tr" for each sibling to go through table rows and avoid the tooltip*/
			$(this).siblings("tr").each(function() {
				$(this).removeClass("rowSelected");
				/*get id of sibling element and the corresponding rankedPhone variable*/
				var indexSibling = $(this).children('th').first().html();
				var siblingPhone = rankedPhones[indexSibling-1];
				/*get pros/cons containers for sibling and delete its children*/
				compContainers = $(this).find(".compContainer");					
				compContainers.first().empty();
				compContainers.last().empty();					
				
				/*a dictionary on which will loop all comparison items and their better/worse values*/
				comparisonLoop = {"price": ["Cheaper","More expensive"], "rating": ["Better rated by experts", "Rated worse by experts"], 
					"communicate": ["Better for communicating","Worse for communicating"], 
					"photo_video": ["Better for taking photos/videos", "Worse for taking photos/videos"],
					"play_media": ["Better for playing music/videos", "Worse for playing music/videos"],
					 "gaming": ["Better for gaming", "Worse for gaming"]}
				for (var key in comparisonLoop) {
					/*rating is only item where higher is better
					 * remember the higher the value of the ranking the worse the phone is in that aspect*/
					var multiplier = 1;
					if (key == "rating") {
						multiplier = -1;
					};	
					/*if better/worse then add <p> element to appropriate cellContainer together with the
					 * comparison text*/
					if (multiplier * parseFloat(selectedPhone[key]) > multiplier * parseFloat(siblingPhone[key])) {
						var proString = "<p class='cellPros'>" + comparisonLoop[key][0] + "</p>";
						compContainers.first().append(proString);
					} else if (multiplier * parseFloat(selectedPhone[key]) < multiplier * parseFloat(siblingPhone["price"])) {
						var conString = "<p class='cellCons'>" + comparisonLoop[key][1] + "</p>";
						compContainers.last().append(conString);
					};
				};									
			});
		};
	});

	/*when we reach results table, click first element to show by default and move the brand image to the left*/
	if ($("#resultsTable").is(":visible")) {		
		$("tr:eq(1)").trigger("click");
		$(".navbar-header").css({
			"left": "0",
			"transform": "translateX(0%)",
		});
	};
				
	/*show question if appropriate sidebar item clicked*/
	$(document).on("click", "ul li a", function() {
		var index_nav = parseInt($(this).attr("value"));
		var active_selector = ".phoneQform:eq("+ index_nav.toString() + ")";
		var inactive_selector_1 = ".phoneQform:eq("+ ((index_nav+1)%3).toString() + ")";
		var inactive_selector_2 = ".phoneQform:eq("+ ((index_nav+2)%3).toString() + ")";
		$(active_selector).addClass("activeQ").focus();
	});
	
	/*hides the questions div after clicking outside of it"*/
	$(document).mouseup(function(e) {
		var container = $(".activeQ");
		// if the target of the click isn't the container nor a descendant of the container
		if (!container.is(e.target) && container.has(e.target).length === 0) 
		{
			container.removeClass("activeQ");
		}
	});
	/*hides the questions div if you click on the closeButton*/
	$(".closeButton").on("click", function() {
		$(".activeQ").removeClass("activeQ");
	});
		
	/*add user's location when feedback form loaded up
	 *https://stackoverflow.com/questions/391979/how-to-get-clients-ip-address-using-javascript-only*/
	if ($("#id_content").is(":visible")) {
		$.getJSON('//freegeoip.net/json/?callback=?', function(data) {
			$("#id_location").val(JSON.stringify(data, null, 2));
		});	
	}
});

