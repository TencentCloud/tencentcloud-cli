**Example 1: 数学试题识别示例代码**



Input: 

```
tccli ocr EduPaperOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "QuestionBlockInfos": [
            {
                "QuestionBboxCoord": {
                    "Y": 0,
                    "X": 0,
                    "Width": 0,
                    "Height": 0
                },
                "QuestionArr": [
                    {
                        "QuestionTextNo": "",
                        "QuestionTextType": 3,
                        "QuestionImageCoords": [
                            {
                                "Y": 0,
                                "X": 0,
                                "Width": 0,
                                "Height": 0
                            }
                        ],
                        "QuestionText": "题型4:已知函数的单调性求参数的取值范围",
                        "QuestionOptions": "[{\"option\":[]}]",
                        "QuestionSubquestion": "[]"
                    }
                ]
            },
            {
                "QuestionBboxCoord": {
                    "Y": 0,
                    "X": 0,
                    "Width": 0,
                    "Height": 0
                },
                "QuestionArr": [
                    {
                        "QuestionTextNo": "[例9]",
                        "QuestionTextType": 3,
                        "QuestionImageCoords": [
                            {
                                "Y": 0,
                                "X": 0,
                                "Width": 0,
                                "Height": 0
                            }
                        ],
                        "QuestionText": "(★★★)已知函数f(x)=\\frac{ax+1}{x+2}在区间(-2,+∞)上是增函数,试求a的取值范围.",
                        "QuestionOptions": "[{\"option\":[]}]",
                        "QuestionSubquestion": "[]"
                    }
                ]
            },
            {
                "QuestionBboxCoord": {
                    "Y": 0,
                    "X": 0,
                    "Width": 0,
                    "Height": 0
                },
                "QuestionArr": [
                    {
                        "QuestionTextNo": "[例10]",
                        "QuestionTextType": 1,
                        "QuestionImageCoords": [
                            {
                                "Y": 0,
                                "X": 0,
                                "Width": 0,
                                "Height": 0
                            }
                        ],
                        "QuestionText": "(★★★★)已知函数,若f(x)=\\left\\lbrace\\begin{array}{l}{(2a-1)x+a,}&{x\\geq1}\\\\{\\log_{a}x,}&{x&lt1}\\end{array}\\right.在(0,+∞)上单调递减，则a的取值范围为##{()}##",
                        "QuestionOptions": "[{\"option\":[\"$${\\\\quad(0,\\\\frac{1}{2})}$$\",\"$${\\\\quad(0,\\\\frac{1}{3}\\\\rbrack}$$\",\"$${\\\\quad\\\\lbrack\\\\frac{1}{3},\\\\frac{1}{2})}$$\",\"$${\\\\quad(\\\\frac{1}{2},1)}$$\"]}]",
                        "QuestionSubquestion": "[]"
                    }
                ]
            },
            {
                "QuestionBboxCoord": {
                    "Y": 0,
                    "X": 0,
                    "Width": 0,
                    "Height": 0
                },
                "QuestionArr": [
                    {
                        "QuestionTextNo": "[例11]",
                        "QuestionTextType": 1,
                        "QuestionImageCoords": [
                            {
                                "Y": 0,
                                "X": 0,
                                "Width": 0,
                                "Height": 0
                            }
                        ],
                        "QuestionText": "(★★★★★)设f(x)=\\left\\lbrace\\begin{array}{l}{a^{x},}&{x&lt0}\\\\{(a-3)x+4a,x\\geq0}\\end{array}\\right.，对任意的.x_{1}\\neqx_{2}都有\\frac{f(x_{1})-f(x_{2})}{x_{1}-x_{2}}&lt0成立，则a的取值范围是##{()}##",
                        "QuestionOptions": "[{\"option\":[\"$${\\\\quad(0,\\\\frac{1}{4}\\\\rbrack}$$\",\"(0,1)\",\"$${\\\\quad\\\\lbrack\\\\frac{1}{4},1)}$$\",\"(0,3)\"]}]",
                        "QuestionSubquestion": "[]"
                    }
                ]
            }
        ],
        "EduPaperInfos": [
            {
                "Item": "0",
                "DetectedText": "\\frac { f ( x _ { 1 } ) - f ( x _ { 2 } ) } { x _ { 1 } - x _ { 2 } } &lt 0  ",
                "Itemcoord": {
                    "X": 1188,
                    "Y": 1320,
                    "Width": 224,
                    "Height": 84
                }
            },
            {
                "Item": "0",
                "DetectedText": "f ( x ) = \\frac { a x + 1 } { x + 2 }  ",
                "Itemcoord": {
                    "X": 537,
                    "Y": 335,
                    "Width": 169,
                    "Height": 63
                }
            },
            {
                "Item": "0",
                "DetectedText": "D . \\quad ( \\frac { 1 } { 2 } , 1 )  ",
                "Itemcoord": {
                    "X": 1163,
                    "Y": 900,
                    "Width": 156,
                    "Height": 79
                }
            },
            {
                "Item": "0",
                "DetectedText": "C . \\quad \\lbrack \\frac { 1 } { 3 } , \\frac { 1 } { 2 } )  ",
                "Itemcoord": {
                    "X": 872,
                    "Y": 900,
                    "Width": 160,
                    "Height": 80
                }
            },
            {
                "Item": "0",
                "DetectedText": "B . \\quad ( 0 , \\frac { 1 } { 3 } \\rbrack  ",
                "Itemcoord": {
                    "X": 580,
                    "Y": 899,
                    "Width": 159,
                    "Height": 82
                }
            },
            {
                "Item": "0",
                "DetectedText": "A . \\quad ( 0 , \\frac { 1 } { 4 } \\rbrack  ",
                "Itemcoord": {
                    "X": 273,
                    "Y": 1499,
                    "Width": 163,
                    "Height": 79
                }
            },
            {
                "Item": "0",
                "DetectedText": "C . \\quad \\lbrack \\frac { 1 } { 4 } , 1 )  ",
                "Itemcoord": {
                    "X": 872,
                    "Y": 1495,
                    "Width": 148,
                    "Height": 81
                }
            },
            {
                "Item": "0",
                "DetectedText": "A . \\quad ( 0 , \\frac { 1 } { 2 } )  ",
                "Itemcoord": {
                    "X": 289,
                    "Y": 900,
                    "Width": 162,
                    "Height": 79
                }
            },
            {
                "Item": "0",
                "DetectedText": "f ( x ) = \\left\\lbrace\\begin{array}{l} { ( 2 a - 1 ) x + a , } & { x \\geq 1 } \\\\ { \\log _ { a } x , } & { x &lt 1 } \\end{array}\\right.  ",
                "Itemcoord": {
                    "X": 641,
                    "Y": 727,
                    "Width": 364,
                    "Height": 89
                }
            },
            {
                "Item": "0",
                "DetectedText": "f ( x ) = \\left\\lbrace\\begin{array}{l} { a ^ { x } , } & { x &lt 0 } \\\\ { ( a - 3 ) x + 4 a , x \\geq 0 } \\end{array}\\right.  ",
                "Itemcoord": {
                    "X": 514,
                    "Y": 1313,
                    "Width": 391,
                    "Height": 96
                }
            },
            {
                "Item": "0",
                "DetectedText": "x _ { 1 } \\neq x _ { 2 }  ",
                "Itemcoord": {
                    "X": 1040,
                    "Y": 1351,
                    "Width": 85,
                    "Height": 29
                }
            },
            {
                "Item": "1000",
                "DetectedText": "题型4:已知函数的单调性求参数的取值范围",
                "Itemcoord": {
                    "X": 282,
                    "Y": 233,
                    "Width": 765,
                    "Height": 41
                }
            },
            {
                "Item": "1000",
                "DetectedText": "[例9] (★★★) 已知函数",
                "Itemcoord": {
                    "X": 194,
                    "Y": 347,
                    "Width": 342,
                    "Height": 33
                }
            },
            {
                "Item": "1000",
                "DetectedText": "在区间(-2, +∞)上是增函数,试求a的取值范围.",
                "Itemcoord": {
                    "X": 708,
                    "Y": 345,
                    "Width": 634,
                    "Height": 37
                }
            },
            {
                "Item": "1000",
                "DetectedText": "[例10] (★★★★) 已知函数,若",
                "Itemcoord": {
                    "X": 193,
                    "Y": 749,
                    "Width": 447,
                    "Height": 38
                }
            },
            {
                "Item": "1000",
                "DetectedText": "在(0, +∞)上单调递减，则a的取",
                "Itemcoord": {
                    "X": 1029,
                    "Y": 747,
                    "Width": 444,
                    "Height": 38
                }
            },
            {
                "Item": "1000",
                "DetectedText": "值范围为( )",
                "Itemcoord": {
                    "X": 282,
                    "Y": 841,
                    "Width": 214,
                    "Height": 37
                }
            },
            {
                "Item": "1000",
                "DetectedText": "[例11] (★★★★★)设",
                "Itemcoord": {
                    "X": 194,
                    "Y": 1343,
                    "Width": 319,
                    "Height": 39
                }
            },
            {
                "Item": "1000",
                "DetectedText": "，对任意的.",
                "Itemcoord": {
                    "X": 914,
                    "Y": 1345,
                    "Width": 125,
                    "Height": 34
                }
            },
            {
                "Item": "1000",
                "DetectedText": "都有",
                "Itemcoord": {
                    "X": 1127,
                    "Y": 1345,
                    "Width": 55,
                    "Height": 34
                }
            },
            {
                "Item": "1000",
                "DetectedText": "成立，",
                "Itemcoord": {
                    "X": 1414,
                    "Y": 1346,
                    "Width": 67,
                    "Height": 32
                }
            },
            {
                "Item": "1000",
                "DetectedText": "则a的取值范围是( )",
                "Itemcoord": {
                    "X": 282,
                    "Y": 1434,
                    "Width": 336,
                    "Height": 42
                }
            },
            {
                "Item": "1000",
                "DetectedText": "B. (0, 1)",
                "Itemcoord": {
                    "X": 589,
                    "Y": 1515,
                    "Width": 128,
                    "Height": 38
                }
            },
            {
                "Item": "1000",
                "DetectedText": "D. (0,3)",
                "Itemcoord": {
                    "X": 1171,
                    "Y": 1516,
                    "Width": 135,
                    "Height": 37
                }
            },
            {
                "Item": "1000",
                "DetectedText": "2019年高三.数学.寒假文科 ",
                "Itemcoord": {
                    "X": 665,
                    "Y": 2208,
                    "Width": 368,
                    "Height": 33
                }
            },
            {
                "Item": "105",
                "DetectedText": "",
                "Itemcoord": {
                    "X": 406,
                    "Y": 843,
                    "Width": 90,
                    "Height": 35
                }
            },
            {
                "Item": "105",
                "DetectedText": "",
                "Itemcoord": {
                    "X": 524,
                    "Y": 1434,
                    "Width": 94,
                    "Height": 42
                }
            }
        ],
        "RequestId": "ab8a243b-0108-4e44-b3b0-4772b7046fb9"
    }
}
```

