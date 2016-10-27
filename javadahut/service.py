import tornado.ioloop
import tornado.web

HTML_CODE = """
<html>
<head><title><b>Ev's Webpage</b></title>
</head>
<body>
<p><i> ore Mstuff here in italics. </i></p>
<script type="text/javascript">


/*var v = function(p1, p2, p3){
	var text = "";
	for(i = 0; i < p3; i++){
		text += p2;
	}
	return (p1)+(text)+(p1)
}
*/
/*var func = function (newarray){
	var value = ""
	for(i=newarray.length - 1; i >= 0 ; i -= 1){
		value += newarray[i]
	}
	return value;

}*/

//console.log (v("cat", "dog", 6))
//console.log(func(['foo', 'bar', 'baz']))


/*var combine = function(p1, p2){
	var txt = ""
	for(i = 0; i < p3; i++ )
}*/

//console.log 




/*var x = ['foo', 'bar', 'baz'];
var y = [3, 1, 2];
var text = '';
for (var i = 0; i < x.length; i++){
	var word = x[i];
	var number = y[i];
	for 
}*/






/*var par1 = ['foo', 'bar', 'baz']
var par2 = ['baz', 'foo', 'bar']

var cleanup = function(string1, string2){
    var result = "";
    for (var i = 0; i < string1.length; i++){
        if (string[i] === string2[(string2.length - 1 - i)]){
        result += string1[i]
        }
    }
    console.log(result);
}

cleanup(par1, par2);*/








var Puppers = function(name, age, breed, size){
	this.name = name;
	this.age = age;
	this.breed =breed;
	this.size = size;
}
Puppers.prototype.sayHello = function(){
	console.log ("Woof")
}
Puppers.prototype.doggo = function(){
	console.log (this.name+" is a "+ this.breed)
}
Puppers.prototype.bigSmall = function(){
	console.log (this.name+ " is a friendly "this.age+ " year old "+ this.size " puppers.")
}
Puppers.prototype.sayBye = function(){
	console.log (this.name + " says Woof! Woof!")
}

var pup1 = new Puppers("Fido", 1, "Boston Terrier", "medium")
var pup2 = new Puppers("Snoopy", 5, "Beagle", "medium")
var pup3 = new Puppers("Pluto", 3, "Rottweiler", "big")






</script>

</body>
</html>

"""

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(HTML_CODE)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()


