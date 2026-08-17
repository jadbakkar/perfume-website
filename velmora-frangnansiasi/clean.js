const fs = require('fs');
const content = fs.readFileSync('restore_html.py', 'utf-8');

// The Python string is enclosed in """
const startIndex = content.indexOf('"""') + 3;
const endIndex = content.lastIndexOf('"""');
const rawHtml = content.substring(startIndex, endIndex);

// Remove the line numbers
const cleanedHtml = rawHtml.replace(/^\d+:\s?/gm, '');

fs.writeFileSync('index.html', cleanedHtml, 'utf-8');
console.log('Successfully wrote index.html');
