**Example 1: 文档解析示例**

PDF文档解析

Input: 

```
tccli ocr ReconstructDocument --cli-unfold-argument  \
    --FileBase64 data:application/pdf;base64,JVBERi0xLjMKJeLjz9M... \
    --FileType PDF \
    --FileStartPageNumber 1 \
    --FileEndPageNumber 10 \
    --Config.EnableInsetImage True
```

Output: 
```
{
    "Response": {
        "DocumentRecognizeInfo": [
            {
                "Angle": 0,
                "Elements": [
                    {
                        "Elements": null,
                        "Index": 0,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 343,
                                "Y": 71
                            },
                            "LeftTop": {
                                "X": 343,
                                "Y": 56
                            },
                            "RightBottom": {
                                "X": 569,
                                "Y": 71
                            },
                            "RightTop": {
                                "X": 569,
                                "Y": 56
                            }
                        },
                        "Text": "失败乃成功之母，黑暗之后就是光明!",
                        "Type": "header"
                    },
                    {
                        "Elements": null,
                        "Index": 1,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 265,
                                "Y": 393
                            },
                            "LeftTop": {
                                "X": 265,
                                "Y": 271
                            },
                            "RightBottom": {
                                "X": 715,
                                "Y": 393
                            },
                            "RightTop": {
                                "X": 715,
                                "Y": 271
                            }
                        },
                        "Text": "CONSULTANCY AGREEMENT",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 2,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 144,
                                "Y": 558
                            },
                            "LeftTop": {
                                "X": 144,
                                "Y": 536
                            },
                            "RightBottom": {
                                "X": 262,
                                "Y": 558
                            },
                            "RightTop": {
                                "X": 262,
                                "Y": 536
                            }
                        },
                        "Text": "BETWEEN",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 3,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 145,
                                "Y": 644
                            },
                            "LeftTop": {
                                "X": 145,
                                "Y": 623
                            },
                            "RightBottom": {
                                "X": 249,
                                "Y": 644
                            },
                            "RightTop": {
                                "X": 249,
                                "Y": 623
                            }
                        },
                        "Text": " PARTY A",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 4,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 142,
                                "Y": 733
                            },
                            "LeftTop": {
                                "X": 142,
                                "Y": 710
                            },
                            "RightBottom": {
                                "X": 203,
                                "Y": 733
                            },
                            "RightTop": {
                                "X": 203,
                                "Y": 710
                            }
                        },
                        "Text": " AND",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 5,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 144,
                                "Y": 819
                            },
                            "LeftTop": {
                                "X": 144,
                                "Y": 796
                            },
                            "RightBottom": {
                                "X": 249,
                                "Y": 819
                            },
                            "RightTop": {
                                "X": 249,
                                "Y": 796
                            }
                        },
                        "Text": " PARTY B",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 6,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 457,
                                "Y": 1188
                            },
                            "LeftTop": {
                                "X": 457,
                                "Y": 1174
                            },
                            "RightBottom": {
                                "X": 464,
                                "Y": 1188
                            },
                            "RightTop": {
                                "X": 464,
                                "Y": 1174
                            }
                        },
                        "Text": "",
                        "Type": "footer"
                    }
                ],
                "Height": 1263,
                "OriginHeight": 1263,
                "OriginWidth": 893,
                "PageNumber": 0,
                "Width": 893
            },
            {
                "Angle": 0,
                "Elements": [
                    {
                        "Elements": null,
                        "Index": 0,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 344,
                                "Y": 71
                            },
                            "LeftTop": {
                                "X": 344,
                                "Y": 56
                            },
                            "RightBottom": {
                                "X": 569,
                                "Y": 71
                            },
                            "RightTop": {
                                "X": 569,
                                "Y": 56
                            }
                        },
                        "Text": "失败乃成功之母，黑暗之后就是光明!",
                        "Type": "header"
                    },
                    {
                        "Elements": null,
                        "Index": 1,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 118,
                                "Y": 149
                            },
                            "LeftTop": {
                                "X": 118,
                                "Y": 119
                            },
                            "RightBottom": {
                                "X": 425,
                                "Y": 149
                            },
                            "RightTop": {
                                "X": 425,
                                "Y": 119
                            }
                        },
                        "Text": "This agreement is made by and between:",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 2,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 62,
                                "Y": 243
                            },
                            "LeftTop": {
                                "X": 62,
                                "Y": 186
                            },
                            "RightBottom": {
                                "X": 837,
                                "Y": 243
                            },
                            "RightTop": {
                                "X": 837,
                                "Y": 186
                            }
                        },
                        "Text": "PARTYA, a company existing under thlaws ofPeople'sRepublicof China,havingits registeredofficein XXXXXXX",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 3,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 95,
                                "Y": 282
                            },
                            "LeftTop": {
                                "X": 95,
                                "Y": 253
                            },
                            "RightBottom": {
                                "X": 352,
                                "Y": 282
                            },
                            "RightTop": {
                                "X": 352,
                                "Y": 253
                            }
                        },
                        "Text": "(Hereafter refened to as PARTYA\")",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 4,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 92,
                                "Y": 380
                            },
                            "LeftTop": {
                                "X": 92,
                                "Y": 352
                            },
                            "RightBottom": {
                                "X": 316,
                                "Y": 380
                            },
                            "RightTop": {
                                "X": 316,
                                "Y": 352
                            }
                        },
                        "Text": "PARTY B, XXXXXXXXXX",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 5,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 96,
                                "Y": 424
                            },
                            "LeftTop": {
                                "X": 96,
                                "Y": 398
                            },
                            "RightBottom": {
                                "X": 352,
                                "Y": 424
                            },
                            "RightTop": {
                                "X": 352,
                                "Y": 398
                            }
                        },
                        "Text": "(Hereafter referred to asPARTYB\")",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 6,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 447,
                                "Y": 307
                            },
                            "LeftTop": {
                                "X": 447,
                                "Y": 294
                            },
                            "RightBottom": {
                                "X": 488,
                                "Y": 307
                            },
                            "RightTop": {
                                "X": 488,
                                "Y": 294
                            }
                        },
                        "Text": "AND",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 7,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 92,
                                "Y": 493
                            },
                            "LeftTop": {
                                "X": 92,
                                "Y": 464
                            },
                            "RightBottom": {
                                "X": 658,
                                "Y": 493
                            },
                            "RightTop": {
                                "X": 658,
                                "Y": 464
                            }
                        },
                        "Text": "PROJECT: Projects signed with ********.(Hereinafiered to as \"the Project\")",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 8,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 94,
                                "Y": 553
                            },
                            "LeftTop": {
                                "X": 94,
                                "Y": 531
                            },
                            "RightBottom": {
                                "X": 174,
                                "Y": 553
                            },
                            "RightTop": {
                                "X": 174,
                                "Y": 531
                            }
                        },
                        "Text": "Whereas:",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 9,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 152,
                                "Y": 591
                            },
                            "LeftTop": {
                                "X": 152,
                                "Y": 563
                            },
                            "RightBottom": {
                                "X": 737,
                                "Y": 591
                            },
                            "RightTop": {
                                "X": 737,
                                "Y": 563
                            }
                        },
                        "Text": "1.Party A is desirous of cooperating with Party B to carry out the said Project;",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 10,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 151,
                                "Y": 625
                            },
                            "LeftTop": {
                                "X": 151,
                                "Y": 598
                            },
                            "RightBottom": {
                                "X": 475,
                                "Y": 625
                            },
                            "RightTop": {
                                "X": 475,
                                "Y": 598
                            }
                        },
                        "Text": "2.Party B is agreeable to such cooperation;",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 11,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 92,
                                "Y": 690
                            },
                            "LeftTop": {
                                "X": 92,
                                "Y": 661
                            },
                            "RightBottom": {
                                "X": 662,
                                "Y": 690
                            },
                            "RightTop": {
                                "X": 662,
                                "Y": 661
                            }
                        },
                        "Text": "NOW THEREFORE THIS AGREEMENT WITNESSETH AS FOLLOWS:",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 12,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 97,
                                "Y": 748
                            },
                            "LeftTop": {
                                "X": 97,
                                "Y": 730
                            },
                            "RightBottom": {
                                "X": 738,
                                "Y": 748
                            },
                            "RightTop": {
                                "X": 738,
                                "Y": 730
                            }
                        },
                        "Text": "ARITCLE FAPPOINTMENT OF CONSULTANT AND SCOPE OF COOPERATION",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 13,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 112,
                                "Y": 860
                            },
                            "LeftTop": {
                                "X": 112,
                                "Y": 763
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 860
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 763
                            }
                        },
                        "Text": "1.1 Party A hereby appoints Party B as its consultants for the Projects in XXXX (COUNTRY)CLIENT, subject to the terms and conditions of this Agreement. The consultants accept such appointme and agree to keep, observe and perform the terms and conditions of the Agreement.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 14,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 110,
                                "Y": 928
                            },
                            "LeftTop": {
                                "X": 110,
                                "Y": 865
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 928
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 865
                            }
                        },
                        "Text": "1.2 Party B shall not provide third parties of a competitive nature the same service as provided to Party A, for the same project throughout the effective term of this Agreement.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 15,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 148,
                                "Y": 963
                            },
                            "LeftTop": {
                                "X": 148,
                                "Y": 933
                            },
                            "RightBottom": {
                                "X": 889,
                                "Y": 963
                            },
                            "RightTop": {
                                "X": 889,
                                "Y": 933
                            }
                        },
                        "Text": "1.3 The service contemplated under this Agreement shall be restricted in XXXX(COUNTRY).",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 16,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 97,
                                "Y": 1021
                            },
                            "LeftTop": {
                                "X": 97,
                                "Y": 1003
                            },
                            "RightBottom": {
                                "X": 534,
                                "Y": 1021
                            },
                            "RightTop": {
                                "X": 534,
                                "Y": 1003
                            }
                        },
                        "Text": "ARTICLE 2-SUBJECT MATTER OF THE AGREEMENT",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 17,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 58,
                                "Y": 1096
                            },
                            "LeftTop": {
                                "X": 58,
                                "Y": 1036
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 1096
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 1036
                            }
                        },
                        "Text": "2.1 The parties shall cooperate with each other in accordance with obligations and conditions containe herein the Agreement.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 18,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 99,
                                "Y": 1156
                            },
                            "LeftTop": {
                                "X": 99,
                                "Y": 1139
                            },
                            "RightBottom": {
                                "X": 414,
                                "Y": 1156
                            },
                            "RightTop": {
                                "X": 414,
                                "Y": 1139
                            }
                        },
                        "Text": "ARTICLE 3OBLIGATION OF PARTY B",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 19,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 456,
                                "Y": 1189
                            },
                            "LeftTop": {
                                "X": 456,
                                "Y": 1175
                            },
                            "RightBottom": {
                                "X": 467,
                                "Y": 1189
                            },
                            "RightTop": {
                                "X": 467,
                                "Y": 1175
                            }
                        },
                        "Text": "",
                        "Type": "footer"
                    }
                ],
                "Height": 1263,
                "OriginHeight": 1263,
                "OriginWidth": 893,
                "PageNumber": 1,
                "Width": 893
            },
            {
                "Angle": 0,
                "Elements": [
                    {
                        "Elements": null,
                        "Index": 0,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 344,
                                "Y": 71
                            },
                            "LeftTop": {
                                "X": 344,
                                "Y": 56
                            },
                            "RightBottom": {
                                "X": 569,
                                "Y": 71
                            },
                            "RightTop": {
                                "X": 569,
                                "Y": 56
                            }
                        },
                        "Text": "失败乃成功之母，黑暗之后就是光明!",
                        "Type": "header"
                    },
                    {
                        "Elements": null,
                        "Index": 1,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 56,
                                "Y": 240
                            },
                            "LeftTop": {
                                "X": 56,
                                "Y": 111
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 240
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 111
                            }
                        },
                        "Text": "3.1 PARTYB is obligatedto show its capacity by providingall the essential informationadvice,consultation and other services requested by PARTY A, in view of obtaining the project contracts signed betwe PARTY A and the CLIENT and so as to secure the good execution of the contracts by coordination and solving problems occurred between PARTY A and the CLIENT.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 2,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 57,
                                "Y": 406
                            },
                            "LeftTop": {
                                "X": 57,
                                "Y": 278
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 406
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 278
                            }
                        },
                        "Text": "PARTY B will act as a consultant of PARTY A in XXXX (COUNTRY) to promote PARTY A's participatio said Projects in XXXX(COUNTRY), along with XXXX (COUNTRY) authorities and private entities.That con service is not limited in scope but the parties will agree on a list of targets which will constitute the initial basi PARTY B work.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 3,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 93,
                                "Y": 475
                            },
                            "LeftTop": {
                                "X": 93,
                                "Y": 445
                            },
                            "RightBottom": {
                                "X": 727,
                                "Y": 475
                            },
                            "RightTop": {
                                "X": 727,
                                "Y": 445
                            }
                        },
                        "Text": "3.2 Upon the request of PARTY A whenever necessary, PARTY B should also:",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 4,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 110,
                                "Y": 508
                            },
                            "LeftTop": {
                                "X": 110,
                                "Y": 480
                            },
                            "RightBottom": {
                                "X": 524,
                                "Y": 508
                            },
                            "RightTop": {
                                "X": 524,
                                "Y": 480
                            }
                        },
                        "Text": "Provide assistance to PartAs work inthe client's country.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 5,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 55,
                                "Y": 578
                            },
                            "LeftTop": {
                                "X": 55,
                                "Y": 515
                            },
                            "RightBottom": {
                                "X": 839,
                                "Y": 578
                            },
                            "RightTop": {
                                "X": 839,
                                "Y": 515
                            }
                        },
                        "Text": "Supplyto Party A withdata concerningthe marketand other informatiorincludinginformatioron laws,payments, taxatioand other standards in force in the client's country which could be necessary.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 6,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 56,
                                "Y": 646
                            },
                            "LeftTop": {
                                "X": 56,
                                "Y": 584
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 646
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 584
                            }
                        },
                        "Text": "Take part in the preparation and submission of any written document which must be presented to client i relation to the Project.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 7,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 109,
                                "Y": 683
                            },
                            "LeftTop": {
                                "X": 109,
                                "Y": 650
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 683
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 650
                            }
                        },
                        "Text": "Assist Party A to fulfill contractual obligations during the course of implementation of the Project Contr",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 8,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 99,
                                "Y": 739
                            },
                            "LeftTop": {
                                "X": 99,
                                "Y": 724
                            },
                            "RightBottom": {
                                "X": 355,
                                "Y": 739
                            },
                            "RightTop": {
                                "X": 355,
                                "Y": 724
                            }
                        },
                        "Text": "ARTICLE 4CONFIDENTIALITY",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 9,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 56,
                                "Y": 826
                            },
                            "LeftTop": {
                                "X": 56,
                                "Y": 763
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 826
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 763
                            }
                        },
                        "Text": "4.1 The Parties shall keep all information obtained in relation to this Agreement confidential and sha not therefore divulge it to any third parties.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 10,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 93,
                                "Y": 860
                            },
                            "LeftTop": {
                                "X": 93,
                                "Y": 833
                            },
                            "RightBottom": {
                                "X": 707,
                                "Y": 860
                            },
                            "RightTop": {
                                "X": 707,
                                "Y": 833
                            }
                        },
                        "Text": "4.2 Any exception to the above must be agreed to in writing by the Parties.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 11,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 99,
                                "Y": 918
                            },
                            "LeftTop": {
                                "X": 99,
                                "Y": 901
                            },
                            "RightBottom": {
                                "X": 340,
                                "Y": 918
                            },
                            "RightTop": {
                                "X": 340,
                                "Y": 901
                            }
                        },
                        "Text": "ARTICLE 5REMUNERATION",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 12,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 58,
                                "Y": 1030
                            },
                            "LeftTop": {
                                "X": 58,
                                "Y": 971
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 1030
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 971
                            }
                        },
                        "Text": "5.1 Party A shall pay to Party B such remuneration as Party B shall be entitled to in accordance with the terms of this Agreement.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 13,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 57,
                                "Y": 1134
                            },
                            "LeftTop": {
                                "X": 57,
                                "Y": 1071
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 1134
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 1071
                            }
                        },
                        "Text": "5.2 The Parties agree that remuneration shall be paid to PARTY Baccording to the percentage and the contract amount shown in the table below when the contract amount is equal to the bidding price:",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 14,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 456,
                                "Y": 1189
                            },
                            "LeftTop": {
                                "X": 456,
                                "Y": 1175
                            },
                            "RightBottom": {
                                "X": 465,
                                "Y": 1189
                            },
                            "RightTop": {
                                "X": 465,
                                "Y": 1175
                            }
                        },
                        "Text": "",
                        "Type": "footer"
                    }
                ],
                "Height": 1263,
                "OriginHeight": 1263,
                "OriginWidth": 893,
                "PageNumber": 2,
                "Width": 893
            },
            {
                "Angle": 0,
                "Elements": [
                    {
                        "Elements": null,
                        "Index": 0,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 344,
                                "Y": 71
                            },
                            "LeftTop": {
                                "X": 344,
                                "Y": 56
                            },
                            "RightBottom": {
                                "X": 567,
                                "Y": 71
                            },
                            "RightTop": {
                                "X": 567,
                                "Y": 56
                            }
                        },
                        "Text": "失败乃成功之母，黑暗之后就是光明!",
                        "Type": "header"
                    },
                    {
                        "Elements": null,
                        "Index": 1,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 59,
                                "Y": 140
                            },
                            "LeftTop": {
                                "X": 59,
                                "Y": 82
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 140
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 82
                            }
                        },
                        "Text": "When the contract amount is lower than the bidding price, the percentage shown in the table above shall b reduced accordingly upon the Partfiendly discussion.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 2,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 57,
                                "Y": 239
                            },
                            "LeftTop": {
                                "X": 57,
                                "Y": 178
                            },
                            "RightBottom": {
                                "X": 855,
                                "Y": 239
                            },
                            "RightTop": {
                                "X": 855,
                                "Y": 178
                            }
                        },
                        "Text": "5.3 Payments shall be madinto Party B's bank account specified by Party Briting, and shall be in the same currency (USD) as that of the Project contract.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 3,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 57,
                                "Y": 383
                            },
                            "LeftTop": {
                                "X": 57,
                                "Y": 288
                            },
                            "RightBottom": {
                                "X": 850,
                                "Y": 383
                            },
                            "RightTop": {
                                "X": 850,
                                "Y": 288
                            }
                        },
                        "Text": "5.4 In consideration of the fact that Party A shall be paid in accordance wipthythent schedule of the Project contract, payments in favor of Party B shall be made correspondenetly, and shall beten Pdety A's effective receipt of each payment from the Client.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 4,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 99,
                                "Y": 421
                            },
                            "LeftTop": {
                                "X": 99,
                                "Y": 404
                            },
                            "RightBottom": {
                                "X": 379,
                                "Y": 421
                            },
                            "RightTop": {
                                "X": 379,
                                "Y": 404
                            }
                        },
                        "Text": "ARTICLE 6-VALIDITY AND TERM",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 5,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 58,
                                "Y": 538
                            },
                            "LeftTop": {
                                "X": 58,
                                "Y": 444
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 538
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 444
                            }
                        },
                        "Text": "6.1 This Agreement shall come into force on the date of signature and shall remain valid for 1 year. Th Agreement shall remain valid until the end of the Project if the Project is under implemention when this Agreen expires.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 6,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 56,
                                "Y": 686
                            },
                            "LeftTop": {
                                "X": 56,
                                "Y": 556
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 686
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 556
                            }
                        },
                        "Text": "6.2 In the event that the Client unilateraly rescinds the Project contract for any reason before the expriatic of the Project, this agreement shall automatically become ineffectiveness. However, the consultants shall still ma necessary steps to assist PARTY A with the Client to confirm the validity of the part that has been performed a ensure in obtaining the payment equivalent to the value of the part that has been confirmed.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 7,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 63,
                                "Y": 763
                            },
                            "LeftTop": {
                                "X": 63,
                                "Y": 746
                            },
                            "RightBottom": {
                                "X": 295,
                                "Y": 763
                            },
                            "RightTop": {
                                "X": 295,
                                "Y": 746
                            }
                        },
                        "Text": "ARTICLE FORCE MAJEURE",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 8,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 57,
                                "Y": 903
                            },
                            "LeftTop": {
                                "X": 57,
                                "Y": 807
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 903
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 807
                            }
                        },
                        "Text": "7.1 If the Agreement is prevented from execution by force majeure, the prevented party shall promptl inform the other party of the event and the detailed information about the event and the certificate that proves hc the execution of the agreement has been influenced by the events.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 9,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 59,
                                "Y": 1108
                            },
                            "LeftTop": {
                                "X": 59,
                                "Y": 938
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 1108
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 938
                            }
                        },
                        "Text": "7.2 In this Clause,\"Force Majeure\" means an event cannot be forseen by the parties, beyond the cont t of the parties, which makes it impossible for a party to perform its obligation under the Contract, including but limited to: natural calamities; and/or, any change of foreign exchange control policy; and /or, any publication of laws or regulationsas wellas the introductiorof governmentalmeasures or the practicingof administrativacts which may be likely to affect the performance of this agreement.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 10,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 456,
                                "Y": 1189
                            },
                            "LeftTop": {
                                "X": 456,
                                "Y": 1174
                            },
                            "RightBottom": {
                                "X": 465,
                                "Y": 1189
                            },
                            "RightTop": {
                                "X": 465,
                                "Y": 1174
                            }
                        },
                        "Text": "",
                        "Type": "footer"
                    }
                ],
                "Height": 1263,
                "OriginHeight": 1263,
                "OriginWidth": 893,
                "PageNumber": 3,
                "Width": 893
            },
            {
                "Angle": 0,
                "Elements": [
                    {
                        "Elements": null,
                        "Index": 0,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 344,
                                "Y": 71
                            },
                            "LeftTop": {
                                "X": 344,
                                "Y": 56
                            },
                            "RightBottom": {
                                "X": 567,
                                "Y": 71
                            },
                            "RightTop": {
                                "X": 567,
                                "Y": 56
                            }
                        },
                        "Text": "失败乃成功之母，黑暗之后就是光明!",
                        "Type": "header"
                    },
                    {
                        "Elements": null,
                        "Index": 1,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 59,
                                "Y": 140
                            },
                            "LeftTop": {
                                "X": 59,
                                "Y": 82
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 140
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 82
                            }
                        },
                        "Text": "7.3 In case of the Force Majeure, the executing period of the Agreement shall be extended to a period equal to that of the accident.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 2,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 58,
                                "Y": 239
                            },
                            "LeftTop": {
                                "X": 58,
                                "Y": 178
                            },
                            "RightBottom": {
                                "X": 839,
                                "Y": 239
                            },
                            "RightTop": {
                                "X": 839,
                                "Y": 178
                            }
                        },
                        "Text": "7.4 Bothparties shall not demand compensationof each other for losses caused by such a Force Majeure.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 3,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 99,
                                "Y": 318
                            },
                            "LeftTop": {
                                "X": 99,
                                "Y": 301
                            },
                            "RightBottom": {
                                "X": 294,
                                "Y": 318
                            },
                            "RightTop": {
                                "X": 294,
                                "Y": 301
                            }
                        },
                        "Text": "ARTICLE 8-LANGUAGE",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 4,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 57,
                                "Y": 401
                            },
                            "LeftTop": {
                                "X": 57,
                                "Y": 340
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 401
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 340
                            }
                        },
                        "Text": "8.1 All documents, communications or notifications referred to the present Agreement, or which may required under the terms of this Agreement, shall be in English",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 5,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 99,
                                "Y": 461
                            },
                            "LeftTop": {
                                "X": 99,
                                "Y": 444
                            },
                            "RightBottom": {
                                "X": 516,
                                "Y": 461
                            },
                            "RightTop": {
                                "X": 516,
                                "Y": 444
                            }
                        },
                        "Text": "ARTICLE 9GOVERNING LAW AND ARBITRATION",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 6,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 56,
                                "Y": 581
                            },
                            "LeftTop": {
                                "X": 56,
                                "Y": 483
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 581
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 483
                            }
                        },
                        "Text": "9.1 The agreement, includingvithoutlimitatiorits conclusion,validityconstructionperformanceand settlement of disputes, shall be governed by the laws of the People's Republic of China without giving effect to principles of conflict of law.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 7,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 56,
                                "Y": 785
                            },
                            "LeftTop": {
                                "X": 56,
                                "Y": 585
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 785
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 585
                            }
                        },
                        "Text": "9.2 Any disputes arising from, or in connection with the Agreement shall be first settled through frien negotiation by both Parties. In case both Parties reach no settlement to disputes through amicable negotiation, th disputes shall then be submitted to China International Economic and Trade Arbitration Commission f(CIETAC)arbitration in accordance with its Arbitration Rules in force at the time of application for arbitration. The arbitr shall proceed irBEIJING. The arbitral award is final and binding upon both Parties. The arbitration fees shall b borne equally by both parties",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 8,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 56,
                                "Y": 855
                            },
                            "LeftTop": {
                                "X": 56,
                                "Y": 794
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 855
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 794
                            }
                        },
                        "Text": "9.3 To the fullest extent permitted by the law, this arbitration proceeding and the arbitrator's award shall maintained in confidence by the parties so as to protect relevant valuable information or intellectual property righ h",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 9,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 57,
                                "Y": 923
                            },
                            "LeftTop": {
                                "X": 57,
                                "Y": 862
                            },
                            "RightBottom": {
                                "X": 841,
                                "Y": 923
                            },
                            "RightTop": {
                                "X": 841,
                                "Y": 862
                            }
                        },
                        "Text": "9.4 Notwithstandingny referenceto arbitrationboth Parties shall continueto performtheirrespective obligations under the Agreement except for those matters under arbitration.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 10,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 63,
                                "Y": 992
                            },
                            "LeftTop": {
                                "X": 63,
                                "Y": 974
                            },
                            "RightBottom": {
                                "X": 346,
                                "Y": 992
                            },
                            "RightTop": {
                                "X": 346,
                                "Y": 974
                            }
                        },
                        "Text": "ARTICLE 10ENTIRE AGREEMENT",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 11,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 56,
                                "Y": 1111
                            },
                            "LeftTop": {
                                "X": 56,
                                "Y": 1015
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 1111
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 1015
                            }
                        },
                        "Text": "The Agreement and its Annexures constitute the entire Agreement and understanding between the parties wit respect to the subject matter hereof,and there are no additionalor other promises,representations,warranties,agreements, or understandings, whether written or oral, except those as contained herein.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 12,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 456,
                                "Y": 1188
                            },
                            "LeftTop": {
                                "X": 456,
                                "Y": 1174
                            },
                            "RightBottom": {
                                "X": 465,
                                "Y": 1188
                            },
                            "RightTop": {
                                "X": 465,
                                "Y": 1174
                            }
                        },
                        "Text": "",
                        "Type": "footer"
                    }
                ],
                "Height": 1263,
                "OriginHeight": 1263,
                "OriginWidth": 893,
                "PageNumber": 4,
                "Width": 893
            },
            {
                "Angle": 0,
                "Elements": [
                    {
                        "Elements": null,
                        "Index": 0,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 98,
                                "Y": 97
                            },
                            "LeftTop": {
                                "X": 98,
                                "Y": 82
                            },
                            "RightBottom": {
                                "X": 304,
                                "Y": 97
                            },
                            "RightTop": {
                                "X": 304,
                                "Y": 82
                            }
                        },
                        "Text": "ARTICLE 1 FNO WAIVER",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 1,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 343,
                                "Y": 71
                            },
                            "LeftTop": {
                                "X": 343,
                                "Y": 56
                            },
                            "RightBottom": {
                                "X": 569,
                                "Y": 71
                            },
                            "RightTop": {
                                "X": 569,
                                "Y": 56
                            }
                        },
                        "Text": "失败乃成功之母，黑暗之后就是光明!",
                        "Type": "header"
                    },
                    {
                        "Elements": null,
                        "Index": 2,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 57,
                                "Y": 216
                            },
                            "LeftTop": {
                                "X": 57,
                                "Y": 125
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 216
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 125
                            }
                        },
                        "Text": "The failure of either party to insist upon strict adherence to any term or condition of this Agreement on a occasion shall not be considered a waiver or any right to insist upon strict adherence to that term or condition or a other term or condition of this Agreement.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 3,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 99,
                                "Y": 286
                            },
                            "LeftTop": {
                                "X": 99,
                                "Y": 271
                            },
                            "RightBottom": {
                                "X": 373,
                                "Y": 286
                            },
                            "RightTop": {
                                "X": 373,
                                "Y": 271
                            }
                        },
                        "Text": "ARTICLE 12-WRITTEN CHANGES",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 4,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 59,
                                "Y": 371
                            },
                            "LeftTop": {
                                "X": 59,
                                "Y": 308
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 371
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 308
                            }
                        },
                        "Text": "This Agreement may not be altered, modified, amended, changed, rescinded or discharged in whole or in par except by a written Agreement executed by both parties.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 5,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 99,
                                "Y": 428
                            },
                            "LeftTop": {
                                "X": 99,
                                "Y": 413
                            },
                            "RightBottom": {
                                "X": 294,
                                "Y": 428
                            },
                            "RightTop": {
                                "X": 294,
                                "Y": 413
                            }
                        },
                        "Text": "ARTICLE 13-HEADINGS",
                        "Type": "title"
                    },
                    {
                        "Elements": null,
                        "Index": 6,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 57,
                                "Y": 515
                            },
                            "LeftTop": {
                                "X": 57,
                                "Y": 451
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 515
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 451
                            }
                        },
                        "Text": "Headings used in this Agreement are for reference purposes only and shall not in any way affect the meanin or interpretation of this Agreement.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 7,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 58,
                                "Y": 613
                            },
                            "LeftTop": {
                                "X": 58,
                                "Y": 551
                            },
                            "RightBottom": {
                                "X": 893,
                                "Y": 613
                            },
                            "RightTop": {
                                "X": 893,
                                "Y": 551
                            }
                        },
                        "Text": "In witness whereof, the Parties have duly signed the present Agreement in Beijing, RP China, by two origin in English with 7 pages each.",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": [
                            {
                                "Elements": null,
                                "Index": 0,
                                "Level": 1,
                                "Polygon": {
                                    "LeftBottom": {
                                        "X": 94,
                                        "Y": 688
                                    },
                                    "LeftTop": {
                                        "X": 94,
                                        "Y": 663
                                    },
                                    "RightBottom": {
                                        "X": 239,
                                        "Y": 688
                                    },
                                    "RightTop": {
                                        "X": 239,
                                        "Y": 663
                                    }
                                },
                                "Text": "For and behalf of:",
                                "Type": "figure_text"
                            },
                            {
                                "Elements": null,
                                "Index": 1,
                                "Level": 1,
                                "Polygon": {
                                    "LeftBottom": {
                                        "X": 453,
                                        "Y": 688
                                    },
                                    "LeftTop": {
                                        "X": 453,
                                        "Y": 663
                                    },
                                    "RightBottom": {
                                        "X": 597,
                                        "Y": 688
                                    },
                                    "RightTop": {
                                        "X": 597,
                                        "Y": 663
                                    }
                                },
                                "Text": "For and behalf of:",
                                "Type": "figure_text"
                            },
                            {
                                "Elements": null,
                                "Index": 2,
                                "Level": 1,
                                "Polygon": {
                                    "LeftBottom": {
                                        "X": 462,
                                        "Y": 741
                                    },
                                    "LeftTop": {
                                        "X": 462,
                                        "Y": 717
                                    },
                                    "RightBottom": {
                                        "X": 568,
                                        "Y": 741
                                    },
                                    "RightTop": {
                                        "X": 568,
                                        "Y": 717
                                    }
                                },
                                "Text": "PARTY B",
                                "Type": "figure_text"
                            },
                            {
                                "Elements": null,
                                "Index": 3,
                                "Level": 1,
                                "Polygon": {
                                    "LeftBottom": {
                                        "X": 94,
                                        "Y": 742
                                    },
                                    "LeftTop": {
                                        "X": 94,
                                        "Y": 719
                                    },
                                    "RightBottom": {
                                        "X": 181,
                                        "Y": 742
                                    },
                                    "RightTop": {
                                        "X": 181,
                                        "Y": 719
                                    }
                                },
                                "Text": "PARTY A",
                                "Type": "figure_text"
                            },
                            {
                                "Elements": null,
                                "Index": 4,
                                "Level": 1,
                                "Polygon": {
                                    "LeftBottom": {
                                        "X": 90,
                                        "Y": 799
                                    },
                                    "LeftTop": {
                                        "X": 90,
                                        "Y": 772
                                    },
                                    "RightBottom": {
                                        "X": 130,
                                        "Y": 799
                                    },
                                    "RightTop": {
                                        "X": 130,
                                        "Y": 772
                                    }
                                },
                                "Text": "By",
                                "Type": "figure_text"
                            },
                            {
                                "Elements": null,
                                "Index": 5,
                                "Level": 1,
                                "Polygon": {
                                    "LeftBottom": {
                                        "X": 452,
                                        "Y": 821
                                    },
                                    "LeftTop": {
                                        "X": 452,
                                        "Y": 798
                                    },
                                    "RightBottom": {
                                        "X": 488,
                                        "Y": 821
                                    },
                                    "RightTop": {
                                        "X": 488,
                                        "Y": 798
                                    }
                                },
                                "Text": "By",
                                "Type": "figure_text"
                            },
                            {
                                "Elements": null,
                                "Index": 6,
                                "Level": 1,
                                "Polygon": {
                                    "LeftBottom": {
                                        "X": 94,
                                        "Y": 898
                                    },
                                    "LeftTop": {
                                        "X": 94,
                                        "Y": 879
                                    },
                                    "RightBottom": {
                                        "X": 149,
                                        "Y": 898
                                    },
                                    "RightTop": {
                                        "X": 149,
                                        "Y": 879
                                    }
                                },
                                "Text": "Name",
                                "Type": "figure_text"
                            },
                            {
                                "Elements": null,
                                "Index": 7,
                                "Level": 1,
                                "Polygon": {
                                    "LeftBottom": {
                                        "X": 453,
                                        "Y": 908
                                    },
                                    "LeftTop": {
                                        "X": 453,
                                        "Y": 888
                                    },
                                    "RightBottom": {
                                        "X": 508,
                                        "Y": 908
                                    },
                                    "RightTop": {
                                        "X": 508,
                                        "Y": 888
                                    }
                                },
                                "Text": "Name",
                                "Type": "figure_text"
                            },
                            {
                                "Elements": null,
                                "Index": 8,
                                "Level": 1,
                                "Polygon": {
                                    "LeftBottom": {
                                        "X": 96,
                                        "Y": 953
                                    },
                                    "LeftTop": {
                                        "X": 96,
                                        "Y": 934
                                    },
                                    "RightBottom": {
                                        "X": 140,
                                        "Y": 953
                                    },
                                    "RightTop": {
                                        "X": 140,
                                        "Y": 934
                                    }
                                },
                                "Text": "Title",
                                "Type": "figure_text"
                            },
                            {
                                "Elements": null,
                                "Index": 9,
                                "Level": 1,
                                "Polygon": {
                                    "LeftBottom": {
                                        "X": 455,
                                        "Y": 963
                                    },
                                    "LeftTop": {
                                        "X": 455,
                                        "Y": 943
                                    },
                                    "RightBottom": {
                                        "X": 499,
                                        "Y": 963
                                    },
                                    "RightTop": {
                                        "X": 499,
                                        "Y": 943
                                    }
                                },
                                "Text": "Title",
                                "Type": "figure_text"
                            }
                        ],
                        "Index": 8,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 61,
                                "Y": 963
                            },
                            "LeftTop": {
                                "X": 61,
                                "Y": 663
                            },
                            "RightBottom": {
                                "X": 725,
                                "Y": 963
                            },
                            "RightTop": {
                                "X": 725,
                                "Y": 663
                            }
                        },
                        "Text": "![](61,663,725,963)",
                        "Type": "figure"
                    },
                    {
                        "Elements": null,
                        "Index": 9,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 60,
                                "Y": 1129
                            },
                            "LeftTop": {
                                "X": 60,
                                "Y": 1107
                            },
                            "RightBottom": {
                                "X": 491,
                                "Y": 1129
                            },
                            "RightTop": {
                                "X": 491,
                                "Y": 1107
                            }
                        },
                        "Text": "信你自己罢!只有你自己是真实的，也只有你能够创造你自己",
                        "Type": "paragraph"
                    },
                    {
                        "Elements": null,
                        "Index": 10,
                        "Level": 0,
                        "Polygon": {
                            "LeftBottom": {
                                "X": 456,
                                "Y": 1189
                            },
                            "LeftTop": {
                                "X": 456,
                                "Y": 1174
                            },
                            "RightBottom": {
                                "X": 467,
                                "Y": 1189
                            },
                            "RightTop": {
                                "X": 467,
                                "Y": 1174
                            }
                        },
                        "Text": "6",
                        "Type": "footer"
                    }
                ],
                "Height": 1263,
                "OriginHeight": 1263,
                "OriginWidth": 893,
                "PageNumber": 5,
                "Width": 893
            }
        ],
        "InsetImagePackage": "UEsDBBQACAAIAAAAAAAAAAAAAAAAAAAAAABNAAAAM2UxMjNjYjAtZTkzZ...",
        "RequestId": "3e123cb0-e93e-4ea1-jad4d-9b984b6878cd"
    }
}
```

