**Example 1: 五官定位接口成功示例**

对请求图片进行五官定位。

Input: 

```
tccli iai AnalyzeFace --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg \
    --Mode 0
```

Output: 
```
{
    "Response": {
        "ImageWidth": 550,
        "ImageHeight": 366,
        "FaceShapeSet": [
            {
                "FaceProfile": [
                    {
                        "X": 63,
                        "Y": 335
                    },
                    {
                        "X": 63,
                        "Y": 374
                    },
                    {
                        "X": 66,
                        "Y": 412
                    },
                    {
                        "X": 74,
                        "Y": 450
                    },
                    {
                        "X": 85,
                        "Y": 487
                    },
                    {
                        "X": 100,
                        "Y": 522
                    },
                    {
                        "X": 121,
                        "Y": 554
                    },
                    {
                        "X": 147,
                        "Y": 582
                    },
                    {
                        "X": 176,
                        "Y": 608
                    },
                    {
                        "X": 208,
                        "Y": 627
                    },
                    {
                        "X": 245,
                        "Y": 634
                    },
                    {
                        "X": 282,
                        "Y": 627
                    },
                    {
                        "X": 315,
                        "Y": 607
                    },
                    {
                        "X": 344,
                        "Y": 582
                    },
                    {
                        "X": 370,
                        "Y": 554
                    },
                    {
                        "X": 391,
                        "Y": 522
                    },
                    {
                        "X": 405,
                        "Y": 487
                    },
                    {
                        "X": 416,
                        "Y": 449
                    },
                    {
                        "X": 423,
                        "Y": 411
                    },
                    {
                        "X": 427,
                        "Y": 372
                    },
                    {
                        "X": 426,
                        "Y": 334
                    }
                ],
                "LeftEye": [
                    {
                        "X": 114,
                        "Y": 333
                    },
                    {
                        "X": 128,
                        "Y": 345
                    },
                    {
                        "X": 146,
                        "Y": 349
                    },
                    {
                        "X": 165,
                        "Y": 347
                    },
                    {
                        "X": 183,
                        "Y": 341
                    },
                    {
                        "X": 169,
                        "Y": 325
                    },
                    {
                        "X": 150,
                        "Y": 318
                    },
                    {
                        "X": 130,
                        "Y": 321
                    }
                ],
                "RightEye": [
                    {
                        "X": 378,
                        "Y": 331
                    },
                    {
                        "X": 364,
                        "Y": 343
                    },
                    {
                        "X": 345,
                        "Y": 348
                    },
                    {
                        "X": 327,
                        "Y": 346
                    },
                    {
                        "X": 309,
                        "Y": 340
                    },
                    {
                        "X": 322,
                        "Y": 323
                    },
                    {
                        "X": 341,
                        "Y": 316
                    },
                    {
                        "X": 361,
                        "Y": 319
                    }
                ],
                "LeftEyeBrow": [
                    {
                        "X": 79,
                        "Y": 280
                    },
                    {
                        "X": 108,
                        "Y": 275
                    },
                    {
                        "X": 138,
                        "Y": 274
                    },
                    {
                        "X": 168,
                        "Y": 277
                    },
                    {
                        "X": 198,
                        "Y": 279
                    },
                    {
                        "X": 173,
                        "Y": 256
                    },
                    {
                        "X": 139,
                        "Y": 251
                    },
                    {
                        "X": 105,
                        "Y": 256
                    }
                ],
                "RightEyeBrow": [
                    {
                        "X": 410,
                        "Y": 277
                    },
                    {
                        "X": 380,
                        "Y": 273
                    },
                    {
                        "X": 350,
                        "Y": 272
                    },
                    {
                        "X": 320,
                        "Y": 275
                    },
                    {
                        "X": 290,
                        "Y": 277
                    },
                    {
                        "X": 315,
                        "Y": 255
                    },
                    {
                        "X": 349,
                        "Y": 249
                    },
                    {
                        "X": 384,
                        "Y": 254
                    }
                ],
                "Mouth": [
                    {
                        "X": 173,
                        "Y": 522
                    },
                    {
                        "X": 193,
                        "Y": 541
                    },
                    {
                        "X": 217,
                        "Y": 554
                    },
                    {
                        "X": 244,
                        "Y": 558
                    },
                    {
                        "X": 272,
                        "Y": 554
                    },
                    {
                        "X": 297,
                        "Y": 541
                    },
                    {
                        "X": 317,
                        "Y": 522
                    },
                    {
                        "X": 291,
                        "Y": 517
                    },
                    {
                        "X": 264,
                        "Y": 512
                    },
                    {
                        "X": 245,
                        "Y": 517
                    },
                    {
                        "X": 225,
                        "Y": 512
                    },
                    {
                        "X": 199,
                        "Y": 517
                    },
                    {
                        "X": 196,
                        "Y": 528
                    },
                    {
                        "X": 220,
                        "Y": 532
                    },
                    {
                        "X": 244,
                        "Y": 535
                    },
                    {
                        "X": 269,
                        "Y": 532
                    },
                    {
                        "X": 293,
                        "Y": 528
                    },
                    {
                        "X": 293,
                        "Y": 525
                    },
                    {
                        "X": 269,
                        "Y": 527
                    },
                    {
                        "X": 245,
                        "Y": 530
                    },
                    {
                        "X": 221,
                        "Y": 528
                    },
                    {
                        "X": 197,
                        "Y": 525
                    }
                ],
                "Nose": [
                    {
                        "X": 244,
                        "Y": 428
                    },
                    {
                        "X": 245,
                        "Y": 341
                    },
                    {
                        "X": 231,
                        "Y": 367
                    },
                    {
                        "X": 217,
                        "Y": 392
                    },
                    {
                        "X": 203,
                        "Y": 418
                    },
                    {
                        "X": 187,
                        "Y": 448
                    },
                    {
                        "X": 217,
                        "Y": 464
                    },
                    {
                        "X": 245,
                        "Y": 468
                    },
                    {
                        "X": 272,
                        "Y": 464
                    },
                    {
                        "X": 302,
                        "Y": 448
                    },
                    {
                        "X": 287,
                        "Y": 417
                    },
                    {
                        "X": 273,
                        "Y": 392
                    },
                    {
                        "X": 259,
                        "Y": 366
                    }
                ],
                "LeftPupil": [
                    {
                        "X": 188,
                        "Y": 303
                    }
                ],
                "RightPupil": [
                    {
                        "X": 201,
                        "Y": 304
                    }
                ]
            }
        ],
        "FaceModelVersion": "3.0",
        "RequestId": "a8eb4545-a154-4f86-9510-57a8be9cae0c"
    }
}
```

**Example 2: 五官定位接口异常示例**

对请求图片进行五官定位，图片中无人脸。

Input: 

```
tccli iai AnalyzeFace --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testB.jpg \
    --Mode 0
```

Output: 
```
{
    "Response": {
        "RequestId": "c964ad35-5476-486e-a03f-311faa6652e6",
        "Error": {
            "Code": "InvalidParameterValue.NoFaceInPhoto",
            "Message": "图片中没有人脸。"
        }
    }
}
```

