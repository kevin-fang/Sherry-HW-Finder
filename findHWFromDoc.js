#!/usr/bin/env node
var WordExtractor = require("word-extractor");

function daysInMonth(month,year) {
    return new Date(year, month, 0).getDate();
}

var extracted = new WordExtractor().extract("HW.doc");

var date = new Date();
var today = date.getDate() + 1;
var month = date.getMonth() + 1;
if (today >= daysInMonth(month, date.getYear())) {
  month++;
  today = 1;
}

extracted.then((doc) => {
  var text = doc.getBody();
  var hwSearchRE = ".+" + month + "\/" + today + ".+\n(\t+.+)?"
  var re = new RegExp(hwSearchRE);

  var match = re.exec(text);
  if (match != null) {
    console.log(match[0].trim());
  } else {
    console.log("Incorrect Syllabus/No HW");
  }

});
