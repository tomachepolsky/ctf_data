# Exercise {NUMBER}
How to analyse and obfuscate JavaScript.
Outline: Malicious actors will commonly obfuscate their code, in order to slow down or prevent analysis of artifacts left on a system, this exercise focuses on analysing snippets of code found on a compromised system,
Objective: Analyse the provided obfuscated JavaScript code snippets to extract key information that could be useful in a wider incident investigation.

### Activity Setup Required:
This activity requires the following resources:
+ JSobfuscation-level1.js
+ JSobfuscation-level2.js
+ JSobfuscation-level3.js
+ JSobfuscation-level4.js
+ JSobfuscation-level5_easy.js
+ JSobfuscation-level5_hard.js

Access to the other online resources and text editing tools may also make this exercise easier.
Duration: 60 minutes


## Level 1
```javascript
$(".submit").click(function(event) {
    event.preventDefault()
    var u = $("#user").val();
    var p = $("#pass").val();
    if(u == "admin" && p == String.fromCharCode(74,97,118,97,83,99,114,105,112,116,73,115,83,101,99,117,114,101)) {
        if(document.location.href.indexOf("?p=") == -1) {   
            document.location = document.location.href + "?p=" + p;
        }
    } else {
        $("#response").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
    }
});

```
1. What type of Obfuscation has been used? 
  + `Ascii Char Code Encoding/Decoding`
2. What is the users username? 
  + `Admin`
3. What is the users password?
  + `JavaScriptIsSecure`

---

## Level 2
```javascript
$(".submit").click(function(event) {
    event.preventDefault();
    var p = $("#pass").val();
    if(Sha1.hash(p) == "4096b399c293f8ab6614034000e18288feb911fe") {
        if(document.location.href.indexOf("?p=") == -1) {   
            document.location = document.location.href + "?p=" + p;
        }
    } else {
        $("#response").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
    }
});
```

1. What is the users password?
  + `Highschoolmusical`
2. What type of Obfuscation has been used?
  + `Hashing - SHA1`

---

## Level 3
```javascript
$('.submit')['click'](function () {
    var _0xf382x1 = $('#pass')['val']();
    var _0xf382x2 = '1e';
    var _0xf382x3 = 'lki';
    var _0xf382x4 = '3t1';
    var _0xf382x5 = 'lk';
    if (_0xf382x1 == 'W4' + _0xf382x3 + _0xf382x4 + _0xf382x5 + _0xf382x2) {
        if (document['location']['href']['indexOf']('?p=') == -1) {
            document['location'] = document['location']['href'] + '?p=' + _0xf382x1;
        };
    } else {
        $('#response')['html']('<div class=\'error\'>Wrong password sorry.</div>');
    };
});
```
1. What is the users password?
    + `W4lki3t1lk1e`
2. What type of Obfuscation has been used?
    + `Stacked Strings`
--- 

## Level 4
```javascript
const code = 'ZnVuY3Rpb24ganNPYmZ1c2NhdGlvbjEoKSB7CSAKCWNvbnNvbGUubG9nKCdGTEFHe0pTX0EyQl9CMkF9Jyk7Cn0KanNPYmZ1c2NhdGlvbjEoKTs=';
eval(window.atob(code));
```

1. What type of Obfuscation has been used?
    + `Base64 Encoding/Decoding`
2.	What is the value of the flag?
    + `FLAG{JS_A2B_B2A}`

---

## Level 5 - Easier
```javascript
var x = location.hash;
if (x.charAt(1) == String.fromCharCode(parseInt(97)) && x.charAt(2) == String.fromCharCode(parseInt(110)) && x.charAt(3) == String.fromCharCode(parseInt(99)) && x.charAt(4) == String.fromCharCode(parseInt(104)) && x.charAt(5) == String.fromCharCode(parseInt(111)) && x.charAt(6) == String.fromCharCode(parseInt(114)) && x.charAt(7) == String.fromCharCode(parseInt(101)) && x.charAt(8) == String.fromCharCode(parseInt(100)) && x.charAt(9) == String.fromCharCode(parseInt(106)) && x.charAt(10) == String.fromCharCode(parseInt(97)) && x.charAt(11) == String.fromCharCode(parseInt(118)) && x.charAt(12) == String.fromCharCode(parseInt(97)) && x.charAt(13) == String.fromCharCode(parseInt(115)) && x.charAt(14) == String.fromCharCode(parseInt(99)) && x.charAt(15) == String.fromCharCode(parseInt(114)) && x.charAt(16) == String.fromCharCode(parseInt(105)) && x.charAt(17) == String.fromCharCode(parseInt(112)) && x.charAt(18) == String.fromCharCode(parseInt(116))) {
    var z = x.split("_"),
        y = z[1];
    if (y == md5(z[0])) {
        var ww = btoa(x.substr(1));
        alert("FLAG{" + ww.charAt(4) + ww.charAt(18) + ww.charAt(16) + ww.charAt(15) + ww.charAt(23) + ww.charAt(10) + ww.charAt(2) + ww.charAt(39) + ww.charAt(23) + ww.charAt(18) + ww.charAt(41) + ww.charAt(22) + ww.charAt(27) + ww.charAt(55) + ww.charAt(18) + ww.charAt(41) + ww.charAt(15) + ww.charAt(27) + ww.charAt(2) + ww.charAt(27) + ww.charAt(10) + ww.charAt(0) + ww.charAt(27) + ww.charAt(10) + ww.charAt(55) + ww.charAt(23) + ww.charAt(42) + ww.charAt(2) + "}")
    }
}
```

## Level 5 - Harder
```javascript
var x = location.hash;if (x.charAt(1) == String.fromCharCode(parseInt(97))) {if (x.charAt(2) == String.fromCharCode(parseInt(110))) {if (x.charAt(3) == String.fromCharCode(parseInt(99))) {if (x.charAt(4) == String.fromCharCode(parseInt(104))) {if (x.charAt(5) == String.fromCharCode(parseInt(111))) {if (x.charAt(6) == String.fromCharCode(parseInt(114))) {if (x.charAt(7) == String.fromCharCode(parseInt(101))) {if (x.charAt(8) == String.fromCharCode(parseInt(100))) {if (x.charAt(9) == String.fromCharCode(parseInt(106))) {if (x.charAt(10) == String.fromCharCode(parseInt(97))) {if (x.charAt(11) == String.fromCharCode(parseInt(118))) {if (x.charAt(12) == String.fromCharCode(parseInt(97))) {if (x.charAt(13) == String.fromCharCode(parseInt(115))) {if (x.charAt(14) == String.fromCharCode(parseInt(99))) {if (x.charAt(15) == String.fromCharCode(parseInt(114))) {if (x.charAt(16) == String.fromCharCode(parseInt(105))) {if (x.charAt(17) == String.fromCharCode(parseInt(112))) {if (x.charAt(18) == String.fromCharCode(parseInt(116))) {var z = x.split('_');var y = z[1];if (y == md5(z[0])) {var ww = btoa(x.substr(1));alert("FLAG{" + ww.charAt(4) + ww.charAt(18) + ww.charAt(16) + ww.charAt(15) + ww.charAt(23) + ww.charAt(10) + ww.charAt(2) + ww.charAt(39) + ww.charAt(23) + ww.charAt(18) + ww.charAt(41) + ww.charAt(22) + ww.charAt(27) + ww.charAt(55) + ww.charAt(18) + ww.charAt(41) + ww.charAt(15) + ww.charAt(27) + ww.charAt(2) + ww.charAt(27) + ww.charAt(10) + ww.charAt(0) + ww.charAt(27) + ww.charAt(10) + ww.charAt(55) + ww.charAt(23) + ww.charAt(42) + ww.charAt(2) + "}")}}}}}}}}}}}}}}}}}}}
```

1. What type of Obfuscation has been used?
    + `Base64 Encoding/Decoding`
    + `Ascii CharCode Encoding/Decoding`
    + `Hashing - MD5`
2. What hashing algorithm is used?
    + `MD5`
3. What is the value of the flag?
    + `FLAG{aNch0R5w0NTB31NTh353RY3R10g5}`
4. Using 'https://example.com' as a placeholder, what URI would trigger an alert?
    + `https://example.com#anchoredjavascript_a78c83b4710e8760280c3250858dce48`


---

