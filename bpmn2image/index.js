const {
  convertAll
} = require('bpmn-to-image');

var fs =require('fs');
var path = require("path");

const options = {
	minDimensions: {
		width:400,
		height:300
	},
	title: false,
	footer: false
};

fs.readdir("./files", function(err, files){
	if(err){
		console.log(err);
		return;
	}
	var count = files.length;
	conversions = [];
	for (element of files) {
		// console.log(element);
		png_name = element.replace(".bpmn",".png");
		// console.log(png_name);
		png_path = path.join("images",png_name);
		file_path = path.join("files",element);
		// console.log(png_path);
		conversion = {
 			input: file_path,
			outputs:[png_path]
		};
		conversions.push(conversion)
		
	};
	convertAll(conversions,options);
});




// const conversions = [{
// 	input:'a.bpmn',
// 	outputs:[
// 	'a.png'
// 	]
// }];



// convertAll(
// 	conversions,
// 	options
// );

