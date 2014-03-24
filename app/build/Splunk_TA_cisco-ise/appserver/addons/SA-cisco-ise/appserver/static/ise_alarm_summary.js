require(['jquery'], function($){
    
    $(function() {
	$('#field1').prependTo($('#tblAlarmSummary .panel-body')).find('label').hide();
	$('#field3').prependTo($('#table1 .panel-body')).find('label').hide();
    });
});