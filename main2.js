var change = document.getElementById('cat');
var datas = []

function displayTweet(user, id){
	$("#cat").fadeOut(function(){
		console.log(id)
		var fullurl = "https://publish.twitter.com/oembed?url=https://twitter.com/"+user+"/status/"+id;
		$.getJSON(fullurl,function(data){
			console.log(data.html)
			var fdata = data.html.replace('<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>','');
			change.innerHTML=fdata;
			$.get('https://platform.twitter.com/widgets.js',function(data){
				eval(data)
			});
		});
		$("#cat").fadeIn();
	});
}

function cat(){
	$.get('stuff.txt',function(data){
		datas=data.split('\n');
		b=[]
		datas.forEach(function(dat){
			a=dat.split(' ');
			b.push(a)
		});
		datas=b;
		datas.pop();
		console.log(datas)
		setInterval(function(){safeDisplay()}, 7000);
		safeDisplay();
	});
}

function safeDisplay(){
	temp = datas[0];
	datas.shift();
	if(temp===undefined){
		temp = datas[0];
		datas.shift();
	}
	try{
		displayTweet(temp[0],temp[1])
	}
	catch(err){
		$.get('stuff.txt',function(data){
			datas=data.split('\n');
			b=[]
			datas.forEach(function(dat){
				a=dat.split(' ');
				b.push(a)
			});
			datas=b;
			datas.pop();
			console.log(datas)
			safeDisplay()
		});
	}
}
