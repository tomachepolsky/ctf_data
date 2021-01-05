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

1. What is the users password?
  + `Highschoolmusical`
2. What type of Obfuscation has been used?
  + `Hashing - SHA1`


```

## Level 3
## Level 4
## Level 5 - Easier
## Level 5 - Harder
