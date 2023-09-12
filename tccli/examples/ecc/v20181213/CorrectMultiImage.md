**Example 1: 多图像识别批改-识别**

ServerType = 0，使用识别功能，只返回识别文本。

Input: 

```
tccli ecc CorrectMultiImage --cli-unfold-argument  \
    --InputType 0 \
    --Image https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/0999.jpg https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/1000.jpg \
    --ServerType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": " Dear Peter,\n I am glad to hear from you. Let me tell you something about Nanjing.\nFirst, the environment in Nanjing is beautiful and there are many trees on both sides an of the road\nNext ,it's very easy to travel around the city and there are many ways. People all have a confortable life,here are lots of tall buildings for or them to live.\nWhat's more, Nanjing has many interesting places and lots of visiters come here every year.\nAll in all, Nanjing is a good place to visit Yours sincerely, and I hope you can visit it some day Su Hua\n  Dear Peter,\n I am glad to hear from you. Let me tell you something about Nanjing.\nNanjing is a clean and beautiful city. There a are many trees and mountains. Also, people here live a happy life. They live in comfortable flaks and communicate with their friends easily. And the transport changes. When people want to go out and\ntaxi they can take a or an underground Furthermore, Naying is a good place to travel. There are many places of interest. You can a visit Xuanoun Park. You can see many views in it. All in all, I think Nanjing is a peaceful and Yours sincerely, perfect city. I hope it can be better\nand better. Su Hua\n",
            "CorrectData": null,
            "TaskId": "",
            "SessionId": ""
        },
        "RequestId": "4cd778bd-4e62-44a3-bd6a-27686c2af81d"
    }
}
```

**Example 2: 多图像识别批改-批改**

ServerType = 1，使用批改功能，只返回批改结果。
注意：图像批改耗时较长，超过4s后返回异步任务结果。

Input: 

```
tccli ecc CorrectMultiImage --cli-unfold-argument  \
    --InputType 0 \
    --Image https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/0999.jpg https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/1000.jpg \
    --ServerType 1
```

Output: 
```
{
    "Response": {
        "ResultData": {
            "Content": "",
            "CorrectData": {
                "Score": 63.59,
                "ScoreCat": {
                    "Words": {
                        "Name": "词汇",
                        "Score": 66.15,
                        "Percentage": 42
                    },
                    "Sentences": {
                        "Name": "句子",
                        "Score": 63.9,
                        "Percentage": 28
                    },
                    "Structure": {
                        "Name": "篇章结构",
                        "Score": 57.82,
                        "Percentage": 23
                    },
                    "Content": {
                        "Name": "内容",
                        "Score": 65.96,
                        "Percentage": 7
                    },
                    "Score": 0,
                    "Percentage": 0
                },
                "Comment": "可适当注意词汇积累，多使用一些高级词语；可适当增加复合句和从句的使用；文章衔接不够流畅思路主题尚可，有待提高。请多加练习，更上一层楼。",
                "SentenceComments": [
                    {
                        "Sentence": {
                            "Sentence": "First, the environment in Nanjing is beautiful and there are many trees on both sides an of the road Next ,it's very easy to travel around the city and there are many ways.",
                            "ParaID": 2,
                            "SentenceID": 0
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "连词建议",
                                "Origin": "an",
                                "Replace": "and",
                                "Message": "连接词使用可能不当，请结合上下文确认此处正确的连词，推荐将 an 替换为 and",
                                "ErrorPosition": [
                                    15,
                                    15
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            },
                            {
                                "Type": "Error",
                                "ErrorType": "标点错误",
                                "Origin": "",
                                "Replace": ".",
                                "Message": "标点符号缺失，请检查断句是否合理，需要插入 .",
                                "ErrorPosition": [
                                    18,
                                    19
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "People all have a confortable life,here are lots of tall buildings for or them to live.",
                            "ParaID": 2,
                            "SentenceID": 1
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "拼写错误",
                                "Origin": "confortable",
                                "Replace": "comfortable",
                                "Message": "confortable 可能是拼写错误，请注意拼写检查，这里应将 confortable 替换为 comfortable",
                                "ErrorPosition": [
                                    4,
                                    4
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            },
                            {
                                "Type": "Error",
                                "ErrorType": "标点建议",
                                "Origin": ",",
                                "Replace": ".",
                                "Message": "标点符号可能使用不当，请检查断句情况，推荐将 , 替换为 .",
                                "ErrorPosition": [
                                    5,
                                    5
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            },
                            {
                                "Type": "Error",
                                "ErrorType": "词形错误",
                                "Origin": "here",
                                "Replace": "Here",
                                "Message": "大小写拼写错误,这里应将 here 替换为 Here",
                                "ErrorPosition": [
                                    6,
                                    6
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            },
                            {
                                "Type": "Error",
                                "ErrorType": "介词错误",
                                "Origin": "",
                                "Replace": "for",
                                "Message": "介词缺失，需要插入 for",
                                "ErrorPosition": [
                                    13,
                                    14
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "What's more, Nanjing has many interesting places and lots of visiters come here every year.",
                            "ParaID": 3,
                            "SentenceID": 0
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "拼写错误",
                                "Origin": "visiters",
                                "Replace": "visitors",
                                "Message": "visiters 可能是拼写错误，请注意拼写检查，这里应将 visiters 替换为 visitors",
                                "ErrorPosition": [
                                    10,
                                    10
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "All in all, Nanjing is a good place to visit Yours sincerely, and I hope you can visit it some day Su Hua   Dear Peter,",
                            "ParaID": 4,
                            "SentenceID": 0
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "词形错误",
                                "Origin": "Yours",
                                "Replace": "yours",
                                "Message": "大小写拼写错误,这里应将 Yours 替换为 yours",
                                "ErrorPosition": [
                                    10,
                                    10
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "There a are many trees and mountains.",
                            "ParaID": 6,
                            "SentenceID": 1
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "限定词错误",
                                "Origin": "a",
                                "Replace": "",
                                "Message": "冠词使用多余，请确认是否需要使用不定冠词，应当删除 ",
                                "ErrorPosition": [
                                    1,
                                    1
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "And the transport changes.",
                            "ParaID": 6,
                            "SentenceID": 4
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "限定词建议",
                                "Origin": "the transport",
                                "Replace": "transportation",
                                "Message": "可能存在限定词使用错误，请结合上下文分析此处正确的限定词，推荐将 the transport 替换为 transportation",
                                "ErrorPosition": [
                                    1,
                                    2
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "When people want to go out and taxi they can take a or an underground Furthermore, Naying is a good place to travel.",
                            "ParaID": 6,
                            "SentenceID": 5
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "词形错误",
                                "Origin": "Furthermore",
                                "Replace": "furthermore",
                                "Message": "大小写拼写错误,这里应将 Furthermore 替换为 furthermore",
                                "ErrorPosition": [
                                    15,
                                    15
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            },
                            {
                                "Type": "Error",
                                "ErrorType": "语法建议",
                                "Origin": "Naying",
                                "Replace": "saying it",
                                "Message": "可能存在语法错误，推荐将 Naying 替换为 saying it",
                                "ErrorPosition": [
                                    16,
                                    16
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "There are many places of interest.",
                            "ParaID": 6,
                            "SentenceID": 6
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "语法建议",
                                "Origin": "",
                                "Replace": "interesting",
                                "Message": "成分可能缺失，推荐插入 interesting",
                                "ErrorPosition": [
                                    2,
                                    3
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            },
                            {
                                "Type": "Error",
                                "ErrorType": "连词错误",
                                "Origin": "of interest",
                                "Replace": "",
                                "Message": "连词使用多余，请确认此处是否需要使用连词，应当删除 ",
                                "ErrorPosition": [
                                    4,
                                    5
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "You can a visit Xuanoun Park.",
                            "ParaID": 6,
                            "SentenceID": 7
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "限定词错误",
                                "Origin": "a",
                                "Replace": "",
                                "Message": "冠词使用多余，请确认是否需要使用不定冠词，应当删除 ",
                                "ErrorPosition": [
                                    2,
                                    2
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            },
                            {
                                "Type": "Error",
                                "ErrorType": "拼写错误",
                                "Origin": "Xuanoun",
                                "Replace": "unsound",
                                "Message": "xuanoun 可能是拼写错误，请注意拼写检查，这里应将 Xuanoun 替换为 unsound",
                                "ErrorPosition": [
                                    4,
                                    4
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "You can see many views in it.",
                            "ParaID": 6,
                            "SentenceID": 8
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "介词建议",
                                "Origin": "in",
                                "Replace": "from",
                                "Message": "介词使用可能存在不当，请结合语境分析此处正确的介词，推荐将 in 替换为 from",
                                "ErrorPosition": [
                                    5,
                                    5
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "All in all, I think Nanjing is a peaceful and Yours sincerely, perfect city.",
                            "ParaID": 6,
                            "SentenceID": 9
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "词形错误",
                                "Origin": "Yours",
                                "Replace": "yours",
                                "Message": "大小写拼写错误,这里应将 Yours 替换为 yours",
                                "ErrorPosition": [
                                    10,
                                    10
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Sentence": {
                            "Sentence": "I hope it can be better and better.",
                            "ParaID": 6,
                            "SentenceID": 10
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "时态建议",
                                "Origin": "can be",
                                "Replace": "will get",
                                "Message": "可能存在将来时使用错误，请确认时态及将来时的表达方式，推荐将 can be 替换为 will get",
                                "ErrorPosition": [
                                    3,
                                    4
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            0
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        "RequestId": "6560fa28-683e-454f-b8a2-88bee017836a"
    }
}
```

**Example 3: 多图像识别批改-异步批改**

ServerType = 1，使用批改功能，只返回批改结果。
IsAsync= 1，使用异步处理。

Input: 

```
tccli ecc CorrectMultiImage --cli-unfold-argument  \
    --InputType 0 \
    --Image https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/0999.jpg https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/1000.jpg \
    --ServerType 1 \
    --IsAsync 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": "",
            "CorrectData": null,
            "TaskId": "10001265",
            "SessionId": ""
        },
        "RequestId": "1d417477-05cb-409e-b4bf-b4a4842ef513"
    }
}
```

