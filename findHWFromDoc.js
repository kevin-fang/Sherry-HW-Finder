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

function extractAndPrint(text, month, today) {
  if (today > 32) {
    return false;
  }
  var hwSearchRE = ".+" + month + "\/" + today + ".+\n(\t+.+)?"
  var re = new RegExp(hwSearchRE);
  var match = re.exec(text);
  if (match != null) {
    console.log(match[0].trim());
    return true;
  }
  return extractAndPrint(text, month, today + 1);
}

extracted.then((doc) => {
  var success = extractAndPrint(doc.getBody(), month, today);
  if (!success) {
    console.log("Incorrect Syllabus/No HW");
  }
});
