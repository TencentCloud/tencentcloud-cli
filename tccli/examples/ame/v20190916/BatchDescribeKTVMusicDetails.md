**Example 1: 查询直播互动曲目详情列表**

查询直播互动曲目详情列表

Input: 

```
tccli ame BatchDescribeKTVMusicDetails --cli-unfold-argument  \
    --MusicIds 0000e1f4-502f-4fbc-857b-6dbad90f9802 a
```

Output: 
```
{
    "Response": {
        "KTVMusicDetailInfoSet": [
            {
                "ChorusClipSet": [
                    {
                        "EndTime": 109250,
                        "StartTime": 64387
                    }
                ],
                "DefinitionInfoSet": [
                    {
                        "Bitrate": 64000,
                        "Definition": "audio/mi",
                        "Size": 1992000
                    },
                    {
                        "Bitrate": 128000,
                        "Definition": "audio/lo",
                        "Size": 3984000
                    }
                ],
                "KTVMusicBaseInfo": {
                    "ComposerSet": [
                        ""
                    ],
                    "Duration": 249,
                    "LyricistSet": [
                        ""
                    ],
                    "MusicId": "0000e1f4-502f-4fbc-857b-6dbad90f9802",
                    "Name": "我的故事我的歌",
                    "SingerInfoSet": [
                        {
                            "Name": "后来者",
                            "SingerId": "05ce39873cc7476ca987d0c621b18ee6"
                        }
                    ],
                    "SingerSet": [
                        "后来者"
                    ],
                    "TagSet": [
                        "故事情节",
                        "情歌"
                    ]
                },
                "LyricsUrl": "https://1500005072.vod2.myqcloud.com/6c9a2f96vodcq1500005072/799b51c33701925920835211299/subtitles/ame-subtitle.vtt?sign=4378ec47c23996d25fe07dc823dff306&t=620dcad9&us=1300054767",
                "PreludeInterval": 0,
                "MidiJsonUrl": "https://smart-media-prod-1258642396.file.myqcloud.com/midijson/0000e1f4-502f-4fbc-857b-6dbad90f9802/b2f9a8d1b8f34e86baece70246a8a55b_1640942219276.json?sign=e471c221033bdca7692909a339ac79fe&t=1645067465",
                "PlayToken": "eyJNdXNpY0lkIjoiMDAwMGUxZjQtNTAyZi00ZmJjLTg1N2ItNmRiYWQ5MGY5ODAyIiwiRmlsZUlkIjoiMzcwMTkyNTkyMDgzNTIxMTI5OSIsIlBsYXlTaWduIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmhjSEJKWkNJNk1UVXdNREF3TlRBM01pd2lZM1Z5Y21WdWRGUnBiV1ZUZEdGdGNDSTZNVFkwTlRBMk56UTJOU3dpWlhod2FYSmxWR2x0WlZOMFlXMXdJam94TmpRMU1EY3hNRFkxTENKbWFXeGxTV1FpT2lJek56QXhPVEkxT1RJd09ETTFNakV4TWprNUlpd2ljR05tWnlJNkltRnRaVVJ5YlRrd01ETWlMQ0oxY214QlkyTmxjM05KYm1adklqcDdJblFpT2lJMk1qQmtZMkZrT1NKOWZRLkJKVmg4U0RJSnhGX3REWklDZjZ4NXRtQzZYNmNEZDFLa0s0WDJGUld1S2ciLCJSZXBvcnRLZXkiOiJleUpoYkdjaU9pSklVelV4TWlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKQmNIQkpaQ0k2TVRNd01EQTFORGMyTnl3aVRYVnphV05KWkNJNklqQXdNREJsTVdZMExUVXdNbVl0TkdaaVl5MDROVGRpTFRaa1ltRmtPVEJtT1Rnd01pSXNJa2xRSWpvaU1URXVNVE0xTGpVdU1UY3lJaXdpVW1Wd2IzSjBWR2x0WlNJNklqSXdNakl0TURJdE1UY2dNVEU2TVRFNk1EVWlMQ0psZUhBaU9qRTJORFV3TnpRMk5qVXVOak0zTnpRNUxDSnBjM01pT2lKVFpYSjJhV05sSW4wLmVYQ2RiQzRFXzVtTHItNlBZZGMyVmlCSFE0VXd1akUxUDZYNFo3T3E0VXc0enZfMXJtcVRCcHBfQng3YWFnaVV3al9iRF85cG01eVhEbC16bkNnX3Z3IiwiVm9kQXBwSWQiOjE1MDAwMDUwNzJ9"
            }
        ],
        "NotExistMusicIdSet": [
            "a"
        ],
        "RequestId": "c163a5b7-b4c9-4b71-9202-81532d9c69dc"
    }
}
```

