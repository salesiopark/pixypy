setInterval( function() {
    $.getJSON($SCRIPT_ROOT+'/update', function(data) {
        for(let kObjs of Object.keys(data)) {
            for(let kProp of Object.keys(data[kObjs])) {
                objs[kObjs][kProp] = data[kObjs][kProp]
                console.log(kObjs+"."+kProp+"="+data[kObjs][kProp])
            }
        }
    })
}, {{update_time}});
