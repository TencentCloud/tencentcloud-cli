**Example 1: 学科**

学科

Input: 

```
tccli tqi ExtractDialogTags --cli-unfold-argument  \
    --DialogueContents.0.Role 0 \
    --DialogueContents.0.Content 啊对，29号上午。 \
    --DialogueContents.1.Role 0 \
    --DialogueContents.1.Content 呃，上午放假也就中秋节上午放假是吧，对放几天呀。 \
    --DialogueContents.2.Role 0 \
    --DialogueContents.2.Content 放三天吧，可能。 \
    --DialogueContents.3.Role 0 \
    --DialogueContents.3.Content 三天，也就是说呃，加上29号这一天，一共三天是吧。 \
    --DialogueContents.4.Role 0 \
    --DialogueContents.4.Content 呃，啊，对。 \
    --DialogueContents.5.Role 0 \
    --DialogueContents.5.Content 嗯。 \
    --DialogueContents.6.Role 0 \
    --DialogueContents.6.Content 也就是说周一返校是吗？或者说周日的晚上是吗？是啥时候返校呀？ \
    --DialogueContents.7.Role 0 \
    --DialogueContents.7.Content 二号。 \
    --DialogueContents.8.Role 0 \
    --DialogueContents.8.Content 二号返校，10月2号的。 \
    --DialogueContents.9.Role 0 \
    --DialogueContents.9.Content 嗯嗯嗯。 \
    --DialogueContents.10.Role 0 \
    --DialogueContents.10.Content 嗯。 \
    --DialogueContents.11.Role 0 \
    --DialogueContents.11.Content 那也就是说孩子这边的话，课程是可以跟得上的，嗯，那平时平时他应该是住校吧，我看河北我之前去年的时候带的就是河北这边这个省的考生嘛，会比较多一点，嗯，然后很多都是月假的这种，咱们家这边应该也是吧。 \
    --DialogueContents.12.Role 0 \
    --DialogueContents.12.Content 啊，也是月亮。 \
    --DialogueContents.13.Role 0 \
    --DialogueContents.13.Content 嗯，就抓的比较紧，是重点高中衡水中学吗？ \
    --DialogueContents.14.Role 0 \
    --DialogueContents.14.Content 一中二中是是县了的哦，县立高中对那孩子现在成绩如何呀？ \
    --DialogueContents.15.Role 0 \
    --DialogueContents.15.Content 成绩。 \
    --DialogueContents.16.Role 0 \
    --DialogueContents.16.Content 在他班上来说，还是。 \
    --DialogueContents.17.Role 0 \
    --DialogueContents.17.Content 也也也在他班上来说还可以。 \
    --DialogueContents.18.Role 0 \
    --DialogueContents.18.Content 总分大概考多少分？以分数为说。 \
    --DialogueContents.19.Role 0 \
    --DialogueContents.19.Content 他现在不说分，他不会说。 \
    --DialogueContents.20.Role 0 \
    --DialogueContents.20.Content 那咱不不说分数啥意思，就是他学校是按等级制的吗。 \
    --DialogueContents.21.Role 0 \
    --DialogueContents.21.Content 分数。 \
    --DialogueContents.22.Role 0 \
    --DialogueContents.22.Content 对，现在老师不发，孩子不说。 \
    --DialogueContents.23.Role 0 \
    --DialogueContents.23.Content 那您一点都不知道吗？总分考多少分也不知道。 \
    --DialogueContents.24.Role 0 \
    --DialogueContents.24.Content 啊，四百四百四十多分左右吧，哦，那不是知道吗？440分左右。 \
    --DialogueContents.25.Role 0 \
    --DialogueContents.25.Content 对，文科还是理科呀。 \
    --DialogueContents.26.Role 0 \
    --DialogueContents.26.Content 离他选的是五花地。 \
    --DialogueContents.27.Role 0 \
    --DialogueContents.27.Content 物化地。 \
    --DialogueContents.28.Role 0 \
    --DialogueContents.28.Content 对。 \
    --DialogueContents.29.Role 0 \
    --DialogueContents.29.Content 他这个成绩是不是偏科呀，有些学科学的不好呀。 \
    --DialogueContents.30.Role 0 \
    --DialogueContents.30.Content 对，他数学还比较好一点那。 \
    --DialogueContents.31.Role 0 \
    --DialogueContents.31.Content 那那那个英语不大行。 \
    --DialogueContents.32.Role 0 \
    --DialogueContents.32.Content 英语不行。 \
    --DialogueContents.33.Role 0 \
    --DialogueContents.33.Content 对，英语。 \
    --DialogueContents.34.Role 0 \
    --DialogueContents.34.Content 英语语文都不行是吗？ \
    --DialogueContents.35.Role 0 \
    --DialogueContents.35.Content 嗯。 \
    --DialogueContents.36.Role 0 \
    --DialogueContents.36.Content 那他这个薄弱学科的话，您刚才说沟通有问题，孩子长时间住校吗，他这个。 \
    --DialogueContents.37.Role 0 \
    --DialogueContents.37.Content 嗯，这种薄弱学科它是学习方法类的问题，就是说孩子比较努力，但是呢，就是成绩提升比较缓慢，这种没有什么方法。 \
    --DialogueContents.38.Role 0 \
    --DialogueContents.38.Content 嗯，还是说咱们家孩子是这种，就是主观性的问题，就是学习态度，学习习惯的问题。 \
    --DialogueContents.39.Role 0 \
    --DialogueContents.39.Content 学习态度就比如说偷懒了，懒散啦，然后呢就是爱玩啦，然后呢，玩游戏啦。 \
    --DialogueContents.40.Role 0 \
    --DialogueContents.40.Content 叛逆了这种他是哪一种类型的孩子呀？ \
    --DialogueContents.41.Role 0 \
    --DialogueContents.41.Content 他应该是在家了，在在家里的时候反正玩游戏。 \
    --DialogueContents.42.Role 0 \
    --DialogueContents.42.Content 在家不许在家啥呀。 \
    --DialogueContents.43.Role 0 \
    --DialogueContents.43.Content 在家里玩游戏，反正该写的作业也写。 \
    --DialogueContents.44.Role 0 \
    --DialogueContents.44.Content 嗯。 \
    --DialogueContents.45.Role 0 \
    --DialogueContents.45.Content 该写也写，但是呢，你想额外占用他的时间，让他去额外的学习的话，孩子不愿意是吗？ \
    --DialogueContents.46.Role 0 \
    --DialogueContents.46.Content 对。 \
    --DialogueContents.47.Role 0 \
    --DialogueContents.47.Content 嗯。 \
    --DialogueContents.48.Role 0 \
    --DialogueContents.48.Content 那你刚才是有点不听你家长说嘛，他都。 \
    --DialogueContents.49.Role 0 \
    --DialogueContents.49.Content 现在跟他沟通不进去，说了不听。 \
    --DialogueContents.50.Role 0 \
    --DialogueContents.50.Content 不听叛逆有点叛逆是吧。 \
    --DialogueContents.51.Role 0 \
    --DialogueContents.51.Content 嗯. \
    --DialogueType gaotu
```

Output: 
```
{
    "Response": {
        "RequestId": "624fd12a-b839-4852-926a-e4ded28310b4",
        "Tags": [
            {
                "TagName": "学科",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "理科"
                        ]
                    }
                ]
            },
            {
                "TagName": "科目",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "化学",
                            "地理",
                            "物理"
                        ]
                    }
                ]
            },
            {
                "TagName": "补习情况",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "补习班类型",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "学习态度",
                "TagValues": [
                    {
                        "Name": "总体",
                        "Values": [
                            "被动"
                        ]
                    },
                    {
                        "Name": "认真学科",
                        "Values": [
                            "未提及"
                        ]
                    },
                    {
                        "Name": "不认真学科",
                        "Values": [
                            "英语",
                            "语文"
                        ]
                    }
                ]
            },
            {
                "TagName": "状态",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "住校"
                        ]
                    }
                ]
            },
            {
                "TagName": "频率",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "回家时间",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "离家时间",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "薄弱学科",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "英语",
                            "语文"
                        ]
                    }
                ]
            },
            {
                "TagName": "高考地区",
                "TagValues": [
                    {
                        "Name": "省份&直辖市",
                        "Values": [
                            "河北"
                        ]
                    },
                    {
                        "Name": "城市&地区",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "放假信息",
                "TagValues": [
                    {
                        "Name": "是否放假",
                        "Values": [
                            "已放假"
                        ]
                    },
                    {
                        "Name": "放假时间",
                        "Values": [
                            "29号上午"
                        ]
                    }
                ]
            }
        ]
    }
}
```

**Example 2: 补习**

补习

Input: 

```
tccli tqi ExtractDialogTags --cli-unfold-argument  \
    --DialogueContents.0.Role 0 \
    --DialogueContents.0.Content 喂，哎，你好，请问是吴同学的家长吗？ \
    --DialogueContents.1.Role 1 \
    --DialogueContents.1.Content 诶。 \
    --DialogueContents.2.Role 0 \
    --DialogueContents.2.Content 你好，家长，我是高途一对一的回访老师，然后我看到之前呢，咱们有给孩子赠送了一节一对一的薄弱学科试听课，这个课程是一直都没有给孩子安排过，对吧。 \
    --DialogueContents.3.Role 1 \
    --DialogueContents.3.Content 啊，他。 \
    --DialogueContents.4.Role 1 \
    --DialogueContents.4.Content 小播课的他都没看过呢。 \
    --DialogueContents.5.Role 0 \
    --DialogueContents.5.Content 一直都没看过是吗，您是。 \
    --DialogueContents.6.Role 1 \
    --DialogueContents.6.Content 孩子。 \
    --DialogueContents.7.Role 1 \
    --DialogueContents.7.Content 没有看回放哦。 \
    --DialogueContents.8.Role 0 \
    --DialogueContents.8.Content 只看回放孩子是不是，嗯，就是回来家的次数比较少呀。 \
    --DialogueContents.9.Role 0 \
    --DialogueContents.9.Content 然后也没时间上课。 \
    --DialogueContents.10.Role 1 \
    --DialogueContents.10.Content 对，也有这个咱们。 \
    --DialogueContents.11.Role 0 \
    --DialogueContents.11.Content 明白明白，就是我看咱们也给孩子报我们高途的班课，孩子在上班课的时候是只能看回放是吗。 \
    --DialogueContents.12.Role 1 \
    --DialogueContents.12.Content 哎呀。 \
    --DialogueContents.13.Role 0 \
    --DialogueContents.13.Content 明白就是，嗯，马上呢，就要放这个国庆假期了，你看要不就是咱国庆假期的时候，就把孩子这节一对一的这个薄弱学科试听课给孩子安排了，因为咱这个这节课它是专门针对孩子哪一个知识点，他没学会的话，我就老师就给孩子讲哪个知。 \
    --DialogueContents.14.Role 0 \
    --DialogueContents.14.Content 就针对性比较强一些，上一节课就有一节课效果，你看怎么样呢，家长。 \
    --DialogueContents.15.Role 1 \
    --DialogueContents.15.Content 他手机上也。 \
    --DialogueContents.16.Role 1 \
    --DialogueContents.16.Content 一个司机也难。 \
    --DialogueContents.17.Role 1 \
    --DialogueContents.17.Content 那确定对不对哦。 \
    --DialogueContents.18.Role 0 \
    --DialogueContents.18.Content 时间上面不太好确定是吗。 \
    --DialogueContents.19.Role 1 \
    --DialogueContents.19.Content 哎，所以。 \
    --DialogueContents.20.Role 0 \
    --DialogueContents.20.Content 白以而。 \
    --DialogueContents.21.Role 1 \
    --DialogueContents.21.Content 而且里面还有蛮多的作业。在学校里才可。 \
    --DialogueContents.22.Role 0 \
    --DialogueContents.22.Content 哦，孩子嗯，现在的话就是因为咱们这个这节课它是一对一的形式，也就是说孩子啥时候有时间，咱得啥时候孩子啥时候给孩子把这节课给上了，就是孩子昨天放了假之后，如果说我给他约定的这个时间，他嗯要做自己的事情，没有时间上课的话，我到时候可以帮孩子再更换一下上课时间。 \
    --DialogueContents.23.Role 0 \
    --DialogueContents.23.Content 都换到它方便的时候。 \
    --DialogueContents.24.Role 0 \
    --DialogueContents.24.Content 你看这样行不？ \
    --DialogueContents.25.Role 1 \
    --DialogueContents.25.Content 一对一啊，嗯。 \
    --DialogueContents.26.Role 0 \
    --DialogueContents.26.Content 对，一对一的。 \
    --DialogueContents.27.Role 1 \
    --DialogueContents.27.Content 对，他。 \
    --DialogueContents.28.Role 1 \
    --DialogueContents.28.Content 也差不多，以前也算。 \
    --DialogueContents.29.Role 0 \
    --DialogueContents.29.Content 以前上过，上的是哪一种形式，线上还是线下？ \
    --DialogueContents.30.Role 1 \
    --DialogueContents.30.Content 线上的线上的话哦。 \
    --DialogueContents.31.Role 0 \
    --DialogueContents.31.Content 线上的当时效果咋样呀？ \
    --DialogueContents.32.Role 1 \
    --DialogueContents.32.Content 也不是很好，不是。 \
    --DialogueContents.33.Role 0 \
    --DialogueContents.33.Content 很好，上的是哪一家的呀，500多。 \
    --DialogueContents.34.Role 1 \
    --DialogueContents.34.Content 以前那个。 \
    --DialogueContents.35.Role 1 \
    --DialogueContents.35.Content 那个。 \
    --DialogueContents.36.Role 1 \
    --DialogueContents.36.Content 掌门也学过哦。 \
    --DialogueContents.37.Role 0 \
    --DialogueContents.37.Content 掌门的掌门，他们没有办学格证呀，啊，没们是没有办学资格。 \
    --DialogueContents.38.Role 1 \
    --DialogueContents.38.Content 资格证啊。 \
    --DialogueContents.39.Role 0 \
    --DialogueContents.39.Content 没关系，就是您看，如果说方便的话，我可以先了解一下孩子的这个学习情况，然后呢，我可以免费的先帮孩子做一个学科的一个成绩分析，您觉得我分析的到位了，咱们到时候再帮孩子把这节课给排上，你看咋样？ \
    --DialogueType gaotu
```

Output: 
```
{
    "Response": {
        "RequestId": "eaeaff41-7cd0-4106-a87e-c73e40df020e",
        "Tags": [
            {
                "TagName": "学科",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "科目",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "补习情况",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "有补习"
                        ]
                    }
                ]
            },
            {
                "TagName": "补习班类型",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "高途线上补习班",
                            "非高途线上补习班"
                        ]
                    }
                ]
            },
            {
                "TagName": "学习态度",
                "TagValues": [
                    {
                        "Name": "总体",
                        "Values": [
                            "被动"
                        ]
                    },
                    {
                        "Name": "认真学科",
                        "Values": [
                            "未提及"
                        ]
                    },
                    {
                        "Name": "不认真学科",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "状态",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "频率",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "回家时间",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "离家时间",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "薄弱学科",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "高考地区",
                "TagValues": [
                    {
                        "Name": "省份&直辖市",
                        "Values": [
                            "未提及"
                        ]
                    },
                    {
                        "Name": "城市&地区",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "放假信息",
                "TagValues": [
                    {
                        "Name": "是否放假",
                        "Values": [
                            "已放假"
                        ]
                    },
                    {
                        "Name": "放假时间",
                        "Values": [
                            "昨天"
                        ]
                    }
                ]
            }
        ]
    }
}
```

**Example 3: 薄弱学科**

薄弱学科-未提及

Input: 

```
tccli tqi ExtractDialogTags --cli-unfold-argument  \
    --DialogueContents.0.Role 0 \
    --DialogueContents.0.Content 喂喂，家长您好，呃，您现在是不是给孩子购买这个高途的资料呀，就三本的资料。 \
    --DialogueContents.1.Role 0 \
    --DialogueContents.1.Content 语数英的母题周周通对吧，花了19块钱啊，这个资料的话，会有配套的四千九节的清北名师直播课程，所以说老师跟您联系一下，我是负责这次课程的老师高途兰琪老师。 \
    --DialogueContents.2.Role 0 \
    --DialogueContents.2.Content 给您需要给您同步一下我们后续详细的课程安排，包括这个上完课程这个资料好吧。 \
    --DialogueContents.3.Role 1 \
    --DialogueContents.3.Content 你那不是书吗？ \
    --DialogueContents.4.Role 0 \
    --DialogueContents.4.Content 这个书配套的，您当时购书的时候应该知道这个书配套的，会有这个四千九节的清美原师直播课程，这个课程的话和这个书是配套的。 \
    --DialogueContents.5.Role 1 \
    --DialogueContents.5.Content 有什么考？ \
    --DialogueContents.6.Role 0 \
    --DialogueContents.6.Content 里面是四天九节的清北名师直播课程，包含了家长规划课程，包括以后这个选课的课程，以及语、数、英、物化这五大科目的。 \
    --DialogueContents.7.Role 0 \
    --DialogueContents.7.Content 知识点、方法技巧授课，就做题技巧这一方面的授课。 \
    --DialogueContents.8.Role 0 \
    --DialogueContents.8.Content 在这个周五，周六，周日，包括周一。 \
    --DialogueContents.9.Role 0 \
    --DialogueContents.9.Content 呃，您在您已经收到这个课了吗？您已经收到这个书了吗。 \
    --DialogueContents.10.Role 1 \
    --DialogueContents.10.Content 没有没有没有没有，里边还有个卡是吧。 \
    --DialogueContents.11.Role 0 \
    --DialogueContents.11.Content 卡的话没有这个卡吧。 \
    --DialogueContents.12.Role 0 \
    --DialogueContents.12.Content 19的话应该是资料，您当时收货以您收货的这个为主吧，因为您不知道您当时是发的这个19。 \
    --DialogueContents.13.Role 0 \
    --DialogueContents.13.Content 已经给您发送安排安排这个发货，您这两天注意一下您这个物流信息，看看，他是应该是三天左右，三天左右就可以到了。 \
    --DialogueContents.14.Role 0 \
    --DialogueContents.14.Content 应该是没有卡。 \
    --DialogueContents.15.Role 1 \
    --DialogueContents.15.Content 的，你听我说。 \
    --DialogueContents.16.Role 1 \
    --DialogueContents.16.Content 啊。 \
    --DialogueContents.17.Role 0 \
    --DialogueContents.17.Content 这个卡的话应该是没有的吧。 \
    --DialogueContents.18.Role 1 \
    --DialogueContents.18.Content 那不对，他说有卡来着。 \
    --DialogueContents.19.Role 0 \
    --DialogueContents.19.Content 那我不知道您当时购买下单的是哪哪一部分这个资料如果是19块钱的话，应该是这个语数英300。 \
    --DialogueContents.20.Role 1 \
    --DialogueContents.20.Content 块钱的这一部分，他说有个卡在纸上贴着。 \
    --DialogueContents.21.Role 0 \
    --DialogueContents.21.Content 在纸上贴的哦，就是。 \
    --DialogueContents.22.Role 0 \
    --DialogueContents.22.Content 就这个语数英的母题资料对吧。 \
    --DialogueContents.23.Role 0 \
    --DialogueContents.23.Content 是没贴纸。 \
    --DialogueContents.24.Role 1 \
    --DialogueContents.24.Content 上面贴上卡。 \
    --DialogueContents.25.Role 0 \
    --DialogueContents.25.Content 那应该就是他每每本书里面加的有这个相对来说资料吧，因为我不是负责那个资料的一个。 \
    --DialogueContents.26.Role 0 \
    --DialogueContents.26.Content 资料的一个发送，我这边只负责给您安排这个收货。 \
    --DialogueContents.27.Role 1 \
    --DialogueContents.27.Content 就行行行。 \
    --DialogueContents.28.Role 0 \
    --DialogueContents.28.Content 这个没问题，您到时候如果发货的话，肯定是一块给您发过去了。 \
    --DialogueContents.29.Role 0 \
    --DialogueContents.29.Content 对对，后续这个课程需要您，呃，跟我对接一下，因为后续这个课程是我进行负责的，我主要负责这一块。 \
    --DialogueType gaotu
```

Output: 
```
{
    "Response": {
        "RequestId": "283886d1-2b5d-4ae6-8b55-cf19df12bc99",
        "Tags": [
            {
                "TagName": "学科",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "科目",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "补习情况",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "补习班类型",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "学习态度",
                "TagValues": [
                    {
                        "Name": "总体",
                        "Values": [
                            "未提及"
                        ]
                    },
                    {
                        "Name": "认真学科",
                        "Values": [
                            "未提及"
                        ]
                    },
                    {
                        "Name": "不认真学科",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "状态",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "频率",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "回家时间",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "离家时间",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "薄弱学科",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "高考地区",
                "TagValues": [
                    {
                        "Name": "省份&直辖市",
                        "Values": [
                            "未提及"
                        ]
                    },
                    {
                        "Name": "城市&地区",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            }
        ]
    }
}
```

**Example 4: 单个切片标签**

单个切片标签

Input: 

```
tccli tqi ExtractDialogTags --cli-unfold-argument  \
    --DialogueContents.0.Role 0 \
    --DialogueContents.0.Content 那当时你上初中的时候。 \
    --DialogueContents.1.Role 0 \
    --DialogueContents.1.Content 您您那时候有给孩子接触。 \
    --DialogueContents.2.Role 0 \
    --DialogueContents.2.Content 给他报那种补习班，让孩子去补一补这两科嘛。 \
    --DialogueContents.3.Role 1 \
    --DialogueContents.3.Content 补过，在线下补过。 \
    --DialogueContents.4.Role 0 \
    --DialogueContents.4.Content 是那种线下的一对一吗？还是说大班课呀？ \
    --DialogueContents.5.Role 1 \
    --DialogueContents.5.Content 一对一。 \
    --DialogueContents.6.Role 0 \
    --DialogueContents.6.Content 啊。 \
    --DialogueContents.7.Role 0 \
    --DialogueContents.7.Content 补课效果咋样呀，孩子？ \
    --DialogueContents.8.Role 1 \
    --DialogueContents.8.Content 嗯，他那个觉得老师讲的好的，他才。 \
    --DialogueContents.9.Role 1 \
    --DialogueContents.9.Content 行，你觉得不行的，我们就换老师呗。 \
    --DialogueContents.10.Role 0 \
    --DialogueContents.10.Content 哦，就是孩子他自己，嗯，需要对对这个老师的一个要求是比较高一些，需要满足自己的一个。 \
    --DialogueContents.11.Role 0 \
    --DialogueContents.11.Content 就是比较喜欢这个老师，要适应自己的一个讲课风格。 \
    --DialogueContents.12.Role 1 \
    --DialogueContents.12.Content 对呀，他觉得收益还太强。 \
    --DialogueContents.13.Role 1 \
    --DialogueContents.13.Content 要不一般那会儿一对一是也挺贵的。 \
    --DialogueContents.14.Role 0 \
    --DialogueContents.14.Content 嗯，确实。 \
    --DialogueContents.15.Role 1 \
    --DialogueContents.15.Content 嗯。 \
    --DialogueContents.16.Role 0 \
    --DialogueContents.16.Content 嗯，这个我们也是。 \
    --DialogueContents.17.Role 1 \
    --DialogueContents.17.Content 报了这课，想着试听一下。 \
    --DialogueContents.18.Role 0 \
    --DialogueContents.18.Content 那你像孩子的话，他们现在高一这个阶段，他们呃学校现在老师有没有跟他们提过这种呃选科呀之后。 \
    --DialogueContents.19.Role 1 \
    --DialogueContents.19.Content 12月份那个三科。 \
    --DialogueContents.20.Role 0 \
    --DialogueContents.20.Content 那现在呃，孩子他有确定好要选哪些科目吗？ \
    --DialogueContents.21.Role 1 \
    --DialogueContents.21.Content 他目前说要要选文科。 \
    --DialogueContents.22.Role 0 \
    --DialogueContents.22.Content 哦，文科政史地。 \
    --DialogueContents.23.Role 1 \
    --DialogueContents.23.Content 嗯，你说咱们整整十。 \
    --DialogueContents.24.Role 0 \
    --DialogueContents.24.Content 政治、历史和地理。 \
    --DialogueContents.25.Role 1 \
    --DialogueContents.25.Content 他没有说确定哪哈，他就反正说选。 \
    --DialogueContents.26.Role 1 \
    --DialogueContents.26.Content 政治跟历史哪一科没确定哦？ \
    --DialogueContents.27.Role 0 \
    --DialogueContents.27.Content 因为你像现在的话，咱们都是这个新高考，他这个文科。 \
    --DialogueContents.28.Role 1 \
    --DialogueContents.28.Content 分哪个？分政治历史地理还有哪科？ \
    --DialogueContents.29.Role 0 \
    --DialogueContents.29.Content 嗯，没了文科就是你像咱现在的话是新高考，然后之前老高考分文科还有理科，文科的话是政治历史和地理，但是新高考它是不分文理科，而是分物理组和历史组，也就是说物理和历史这两个学科是任选其一，只能选一科，那孩子如果想学文科，那肯定是选择历史。 \
    --DialogueContents.30.Role 1 \
    --DialogueContents.30.Content 怎么着，那理科物理跟那化学还学吗？ \
    --DialogueContents.31.Role 0 \
    --DialogueContents.31.Content 嗯，你像那个物理和历史的话，孩子他如果他是只能选择一科的，他如果选择历史，那剩下的政治地理，还有化学生物这些四科，他在任选两科可以随意选。 \
    --DialogueContents.32.Role 1 \
    --DialogueContents.32.Content 哦，是这么事啊他。 \
    --DialogueContents.33.Role 0 \
    --DialogueContents.33.Content 对对，因为现在是新高考了，就是新高考跟之前的咱老高考那个政策不太一样。 \
    --DialogueContents.34.Role 1 \
    --DialogueContents.34.Content 现在的这个不叫点了吧。 \
    --DialogueContents.35.Role 0 \
    --DialogueContents.35.Content 嗯，可能孩子他应该他是比较平时喜欢这个文科吗？还是说他觉得理科成绩就不太理想，所以就选择选文科。 \
    --DialogueContents.36.Role 1 \
    --DialogueContents.36.Content 他倒是觉得理科成绩不理解这些文科，文科他也比较有有些强盛。 \
    --DialogueContents.37.Role 0 \
    --DialogueContents.37.Content 就是自己也比较擅长对。 \
    --DialogueContents.38.Role 1 \
    --DialogueContents.38.Content 总的理解能力吧。 \
    --DialogueContents.39.Role 1 \
    --DialogueContents.39.Content 背诵也快，理解能力上也也强。 \
    --DialogueContents.40.Role 0 \
    --DialogueContents.40.Content 那孩子语文成绩应该挺好的吧？ \
    --DialogueType gaotu
```

Output: 
```
{
    "Response": {
        "RequestId": "1019e8ce-6c35-4345-8617-1dd18120f629",
        "Tags": [
            {
                "TagName": "学科",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "文科"
                        ]
                    }
                ]
            },
            {
                "TagName": "科目",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "政治",
                            "历史",
                            "地理"
                        ]
                    }
                ]
            },
            {
                "TagName": "补习情况",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "有补习"
                        ]
                    }
                ]
            },
            {
                "TagName": "补习班类型",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "非高途线下补习班"
                        ]
                    }
                ]
            },
            {
                "TagName": "学习态度",
                "TagValues": [
                    {
                        "Name": "总体",
                        "Values": [
                            "主动"
                        ]
                    },
                    {
                        "Name": "认真学科",
                        "Values": [
                            "文科"
                        ]
                    }
                ]
            },
            {
                "TagName": "状态",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "频率",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "回家时间",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "离家时间",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "薄弱学科",
                "TagValues": [
                    {
                        "Name": "",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "高考地区",
                "TagValues": [
                    {
                        "Name": "省份&直辖市",
                        "Values": [
                            "未提及"
                        ]
                    },
                    {
                        "Name": "城市&地区",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            },
            {
                "TagName": "放假信息",
                "TagValues": [
                    {
                        "Name": "是否放假",
                        "Values": [
                            "未提及"
                        ]
                    },
                    {
                        "Name": "放假时间",
                        "Values": [
                            "未提及"
                        ]
                    }
                ]
            }
        ]
    }
}
```

**Example 5: 请求大模型错误**

错误

Input: 

```
tccli tqi ExtractDialogTags --cli-unfold-argument  \
    --DialogueContents.0.Role 0 \
    --DialogueContents.0.Content 那当时你上初中的时候。 \
    --DialogueContents.1.Role 0 \
    --DialogueContents.1.Content 您您那时候有给孩子接触。 \
    --DialogueContents.2.Role 0 \
    --DialogueContents.2.Content 给他报那种补习班，让孩子去补一补这两科嘛。 \
    --DialogueContents.3.Role 1 \
    --DialogueContents.3.Content 补过，在线下补过。 \
    --DialogueContents.4.Role 0 \
    --DialogueContents.4.Content 是那种线下的一对一吗？还是说大班课呀？ \
    --DialogueContents.5.Role 1 \
    --DialogueContents.5.Content 一对一。 \
    --DialogueContents.6.Role 0 \
    --DialogueContents.6.Content 啊。 \
    --DialogueContents.7.Role 0 \
    --DialogueContents.7.Content 补课效果咋样呀，孩子？ \
    --DialogueContents.8.Role 1 \
    --DialogueContents.8.Content 嗯，他那个觉得老师讲的好的，他才。 \
    --DialogueContents.9.Role 1 \
    --DialogueContents.9.Content 行，你觉得不行的，我们就换老师呗。 \
    --DialogueContents.10.Role 0 \
    --DialogueContents.10.Content 哦，就是孩子他自己，嗯，需要对对这个老师的一个要求是比较高一些，需要满足自己的一个。 \
    --DialogueContents.11.Role 0 \
    --DialogueContents.11.Content 就是比较喜欢这个老师，要适应自己的一个讲课风格。 \
    --DialogueContents.12.Role 1 \
    --DialogueContents.12.Content 对呀，他觉得收益还太强。 \
    --DialogueContents.13.Role 1 \
    --DialogueContents.13.Content 要不一般那会儿一对一是也挺贵的。 \
    --DialogueContents.14.Role 0 \
    --DialogueContents.14.Content 嗯，确实。 \
    --DialogueContents.15.Role 1 \
    --DialogueContents.15.Content 嗯。 \
    --DialogueContents.16.Role 0 \
    --DialogueContents.16.Content 嗯，这个我们也是。 \
    --DialogueContents.17.Role 1 \
    --DialogueContents.17.Content 报了这课，想着试听一下。 \
    --DialogueContents.18.Role 0 \
    --DialogueContents.18.Content 那你像孩子的话，他们现在高一这个阶段，他们呃学校现在老师有没有跟他们提过这种呃选科呀之后。 \
    --DialogueContents.19.Role 1 \
    --DialogueContents.19.Content 12月份那个三科。 \
    --DialogueContents.20.Role 0 \
    --DialogueContents.20.Content 那现在呃，孩子他有确定好要选哪些科目吗？ \
    --DialogueContents.21.Role 1 \
    --DialogueContents.21.Content 他目前说要要选文科。 \
    --DialogueContents.22.Role 0 \
    --DialogueContents.22.Content 哦，文科政史地。 \
    --DialogueContents.23.Role 1 \
    --DialogueContents.23.Content 嗯，你说咱们整整十。 \
    --DialogueContents.24.Role 0 \
    --DialogueContents.24.Content 政治、历史和地理。 \
    --DialogueContents.25.Role 1 \
    --DialogueContents.25.Content 他没有说确定哪哈，他就反正说选。 \
    --DialogueContents.26.Role 1 \
    --DialogueContents.26.Content 政治跟历史哪一科没确定哦？ \
    --DialogueContents.27.Role 0 \
    --DialogueContents.27.Content 因为你像现在的话，咱们都是这个新高考，他这个文科。 \
    --DialogueContents.28.Role 1 \
    --DialogueContents.28.Content 分哪个？分政治历史地理还有哪科？ \
    --DialogueContents.29.Role 0 \
    --DialogueContents.29.Content 嗯，没了文科就是你像咱现在的话是新高考，然后之前老高考分文科还有理科，文科的话是政治历史和地理，但是新高考它是不分文理科，而是分物理组和历史组，也就是说物理和历史这两个学科是任选其一，只能选一科，那孩子如果想学文科，那肯定是选择历史。 \
    --DialogueContents.30.Role 1 \
    --DialogueContents.30.Content 怎么着，那理科物理跟那化学还学吗？ \
    --DialogueContents.31.Role 0 \
    --DialogueContents.31.Content 嗯，你像那个物理和历史的话，孩子他如果他是只能选择一科的，他如果选择历史，那剩下的政治地理，还有化学生物这些四科，他在任选两科可以随意选。 \
    --DialogueContents.32.Role 1 \
    --DialogueContents.32.Content 哦，是这么事啊他。 \
    --DialogueContents.33.Role 0 \
    --DialogueContents.33.Content 对对，因为现在是新高考了，就是新高考跟之前的咱老高考那个政策不太一样。 \
    --DialogueContents.34.Role 1 \
    --DialogueContents.34.Content 现在的这个不叫点了吧。 \
    --DialogueContents.35.Role 0 \
    --DialogueContents.35.Content 嗯，可能孩子他应该他是比较平时喜欢这个文科吗？还是说他觉得理科成绩就不太理想，所以就选择选文科。 \
    --DialogueContents.36.Role 1 \
    --DialogueContents.36.Content 他倒是觉得理科成绩不理解这些文科，文科他也比较有有些强盛。 \
    --DialogueContents.37.Role 0 \
    --DialogueContents.37.Content 就是自己也比较擅长对。 \
    --DialogueContents.38.Role 1 \
    --DialogueContents.38.Content 总的理解能力吧。 \
    --DialogueContents.39.Role 1 \
    --DialogueContents.39.Content 背诵也快，理解能力上也也强。 \
    --DialogueContents.40.Role 0 \
    --DialogueContents.40.Content 那孩子语文成绩应该挺好的吧？ \
    --DialogueType gaotu
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "请求大模型错误，请稍后重试"
        },
        "RequestId": "91938ba8-65c6-45b4-b0ef-ac8f7a9a0fd0"
    }
}
```

