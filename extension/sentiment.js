/* plan of action:
use window.location.href to get full URL, which can be fed into the python scraper
feed url into scraper, get google links, use links to get websites, perform sentiment analysis on the websites */

// Called when the user clicks on the browser action.
chrome.browserAction.onClicked.addListener(function(tab) {
  console.log('Calculating sentiments of ' + tab.url);
  chrome.tabs.executeScript({
      // stub, append the correct position. current child class name is for the google link, might work?
    code: 'text = document.createTextNode(" \\n Sentiment data goes here."); document.body.appendChild(yuRUbf)'
  });
});