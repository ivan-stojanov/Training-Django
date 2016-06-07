
function init_piechart(count_by_type){
		
		dataSeries = [];
		
		count_by_type.forEach(function(value, index, array) {
			dataSeries[index] = {};
			dataSeries[index]["y"] = value.count;
			dataSeries[index]["name"] = value.itemType__type_name
		});
		
	    $('#container').highcharts({
	        chart: {
	            plotBackgroundColor: null,
	            plotBorderWidth: null,
	            plotShadow: false,
	            type: 'pie'
	        },
	        title: {
	            text: 'Dashboard panel. Statistics about the stock!'
	        },
	        tooltip: {
	            pointFormat: '{series.name}: <b>{point.y} item(s)</b>'
	        },
	        plotOptions: {
	            pie: {
	                allowPointSelect: true,
	                cursor: 'pointer',
	                dataLabels: {
	                    enabled: true,
	                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
	                    style: {
	                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
	                    }
	                }
	            }
	        },
	        series: [{
	            name: 'In stock',
	            colorByPoint: true,
	            data: dataSeries
	        }]
	    });
	}  
