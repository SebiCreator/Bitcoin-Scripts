import os
import inspect
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from src import *

from testmanager import *

raw_transaction1 = "0100000001bf7c629c843cbd1bbefcb9edfd34ea04d7bc60073b5ca4f72078d08903eeeecd4c0000008c493046022100da21a6abf8a6ff1203fc1621542df89c4744cb66926c8853f4cb08ebfbf619fb022100e4ba8389e40afe2e1ed78e6ca5f4d60ba92a9a42b41750c3161cc157f1cb2e6c014104585d10790ce2cc89da52fe79ffb5b897c74736fd26064502878fe5e0167d42fe9e1f08abff0da5257712ccafd018c456f7e066b03800e1db1c3671fe048b7679ffffffff0280969800000000001976a9146a422a63e77af3560ea133ce377604766a6980ef88ac6ad06005000000001976a9147344b5b94753bc2ee1bf87aadbf757864d92d06d88ac00000000"

raw_transaction2 = "0100000005982d651697c22f51f9817f19700464860b82c2e5e7c416ff7deaed0d915cee61000000006c4930460221008dd50aa070b452fee00eda5980deac2b876098a1276fab17c8392f21e6447e050221009f64dfd4a7c9186359e65164c666a2b957f09d376375d0bfe40445adda0e8d3d012103d19f0c8bbcce5daad39865f5efa1acfa9947475cae57ee39cdb393c98cfaa9f3ffffffff0cb6ff24c764a997df3fcd83a4759bf41217adbd1b197048bf705878b1cb45cc010000006b48304502205fdc5a7a457b260ec48da930556704c79c281dea9582d18cd98cbb6cab3d24c7022100f1ed698ed039f17b8b1b468b9e33b156b98169a7add66b685be91667fb0a1ce701210357fc197bc32ff0e75dfc395f744dc7ddf9a4d700bdd3d145db8abb375c280bf8ffffffff808d1afc343260e79449b23edb91ae5b19cad688b08bf8a51690e09f08443567000000006b48304502205e62b787209a233969aefae8990dd361f719188ac9d2034d7ea52e9ae47a828e022100fa4e800ec7280ba36d5d30c1b1c8bd8ba6a690f05148ccc1e2e58ed1849ac1f001210369c37b493cf172dad4b1ee095b0f685b97b8f76fb8a29400fc58adfc7194cfdfffffffffa6a2f83bfdca2f0d70d84227a21f691e4f8fee3239e090abae09c45a21733217010000006a47304402201798b90919f9664ee2180b3762cfa126ab2ecd90a77af8ab87d4b95eb9e2d070022048eb0d4c7f8379596ca3e88d7a3db7f2caf9301417c9e5daa2b8cadecccaecd1012103f5796a4fdb65507def3ad570cc37448539cc7b2567e0fdc0ee8a9c7bf11d02edffffffff969d148141874c9996eb4f83fe5e059f88694a3ba53eac8a45bd66bcb268b964000000006b48304502203cf9b1569453449e423d7307ee85865725b0c170cdec6d657ca78b3709390fe9022100da8ef5410a1ec1097756b8538ba43ac48fb341d4a2e5a49321c76625b7aba9e9012103542c2978b86a67fc2e384cae70e3a323e08925173cac06dcf4ec9a20b981e3c3ffffffff02404b4c00000000001976a91474db47b3163a0acd36a85b269f2dfc0fee9cc91c88ac7c5a0f00000000001976a914767b1de3eb8688cb46bd1e8abb43627cffb668eb88ac00000000"

expected_output1= {
    "versionNr": 1,
    "inputCount": 1,
    "vin": [
        {
            "txid": "cdeeee0389d07820f7a45c3b0760bcd704ea34fdedb9fcbe1bbd3c849c627cbf",
            "vout": 76,
            "ScriptSig": "493046022100da21a6abf8a6ff1203fc1621542df89c4744cb66926c8853f4cb08ebfbf619fb022100e4ba8389e40afe2e1ed78e6ca5f4d60ba92a9a42b41750c3161cc157f1cb2e6c014104585d10790ce2cc89da52fe79ffb5b897c74736fd26064502878fe5e0167d42fe9e1f08abff0da5257712ccafd018c456f7e066b03800e1db1c3671fe048b7679",
            "sequence": 4294967295
        }
    ],
    "outputCount": 2,
    "vout": [
        {
            "value": 0.1,
            "scriptPubKey": "76a9146a422a63e77af3560ea133ce377604766a6980ef88ac"
        },
        {
            "value": 0.9023089,
            "scriptPubKey": "76a9147344b5b94753bc2ee1bf87aadbf757864d92d06d88ac"
        }
    ],
    "locktime": [
        "NoLock",
        -1
    ]
}

expected_output2= {
    "versionNr": 1,
    "inputCount": 5,
    "vin": [
        {
            "txid": "61ee5c910dedea7dff16c4e7e5c2820b86640470197f81f9512fc29716652d98",
            "vout": 0,
            "ScriptSig": "4930460221008dd50aa070b452fee00eda5980deac2b876098a1276fab17c8392f21e6447e050221009f64dfd4a7c9186359e65164c666a2b957f09d376375d0bfe40445adda0e8d3d012103d19f0c8bbcce5daad39865f5efa1acfa9947475cae57ee39cdb393c98cfaa9f3",
            "sequence": 4294967295
        },
        {
            "txid": "cc45cbb1785870bf4870191bbdad1712f49b75a483cd3fdf97a964c724ffb60c",
            "vout": 1,
            "ScriptSig": "48304502205fdc5a7a457b260ec48da930556704c79c281dea9582d18cd98cbb6cab3d24c7022100f1ed698ed039f17b8b1b468b9e33b156b98169a7add66b685be91667fb0a1ce701210357fc197bc32ff0e75dfc395f744dc7ddf9a4d700bdd3d145db8abb375c280bf8",
            "sequence": 4294967295
        },
        {
            "txid": "673544089fe09016a5f88bb088d6ca195bae91db3eb24994e7603234fc1a8d80",
            "vout": 0,
            "ScriptSig": "48304502205e62b787209a233969aefae8990dd361f719188ac9d2034d7ea52e9ae47a828e022100fa4e800ec7280ba36d5d30c1b1c8bd8ba6a690f05148ccc1e2e58ed1849ac1f001210369c37b493cf172dad4b1ee095b0f685b97b8f76fb8a29400fc58adfc7194cfdf",
            "sequence": 4294967295
        },
        {
            "txid": "173273215ac409aeab90e03932ee8f4f1e691fa22742d8700d2fcafd3bf8a2a6",
            "vout": 1,
            "ScriptSig": "47304402201798b90919f9664ee2180b3762cfa126ab2ecd90a77af8ab87d4b95eb9e2d070022048eb0d4c7f8379596ca3e88d7a3db7f2caf9301417c9e5daa2b8cadecccaecd1012103f5796a4fdb65507def3ad570cc37448539cc7b2567e0fdc0ee8a9c7bf11d02ed",
            "sequence": 4294967295
        },
        {
            "txid": "64b968b2bc66bd458aac3ea53b4a69889f055efe834feb96994c874181149d96",
            "vout": 0,
            "ScriptSig": "48304502203cf9b1569453449e423d7307ee85865725b0c170cdec6d657ca78b3709390fe9022100da8ef5410a1ec1097756b8538ba43ac48fb341d4a2e5a49321c76625b7aba9e9012103542c2978b86a67fc2e384cae70e3a323e08925173cac06dcf4ec9a20b981e3c3",
            "sequence": 4294967295
        }
    ],
    "outputCount": 2,
    "vout": [
        {
            "value": 0.05,
            "scriptPubKey": "76a91474db47b3163a0acd36a85b269f2dfc0fee9cc91c88ac"
        },
        {
            "value": 0.01006204,
            "scriptPubKey": "76a914767b1de3eb8688cb46bd1e8abb43627cffb668eb88ac"
        }
    ],
    "locktime": [
        "NoLock",
        -1
    ]
}

handleAssessment(
    func=decodeTransaction,
    input=raw_transaction1,
    output=expected_output1
)

handleAssessment(
    func=decodeTransaction,
    input=raw_transaction2,
    output= expected_output2
)