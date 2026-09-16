**Example 1: 查询通话详情示例**

查询通话详情示例

Input: 

```
tccli ccc DescribeSessionDetail --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SessionId 0f507d5d-e1e4-436e-a655-1d6c75a79b4f \
    --StartTimestamp 1756372067 \
    --EndTimestamp 1756893037
```

Output: 
```
{
    "Response": {
        "AcceptTimestamp": 1756892204,
        "AsrURL": "https:****c*.*cloud.com/tcccadm*n/cdr/*et*sr**xt*key=PEbNJ4*Q**3*pLFHvMinns4n8P*q1n***YbmD**ljz***rb6****B*b*Q*Ag%3D%3D-k-fKVP3WIlGp************************************************************************************************************************************RlBKeW92NFcwV0ZvUklibFl1RExOdkFaSkFONm*q*Wxr*WlCMTFrNmNZWVgrQWdOb*J3OTZzTjJwTWk0UEZ2cS9tZXc*PSIsIm5v**NlIjoiMDd1aFNLRDFmST*4***zNyX9",
        "CallType": 1,
        "Callee": "0086158xxxxxxxx",
        "Caller": "00860755xxxxxxxx",
        "CustomRecordURL": "https://e*am**e.cos.ap-gu*ngzhou.tence**************************************31_f460fff5-0**d-84*4**90*e***76d2.mp3",
        "EndStatus": 1,
        "EndedTimestamp": 1756892230,
        "Events": [
            {
                "EventType": "StaffHold",
                "StaffEventDetail": {
                    "Staffs": [
                        {
                            "Mail": "foo@tencent.com",
                            "StaffNumber": "20012"
                        }
                    ]
                },
                "Timestamp": 1756892209
            },
            {
                "EventType": "StaffUnhold",
                "StaffEventDetail": {
                    "Staffs": [
                        {
                            "Mail": "foo@tencent.com",
                            "StaffNumber": "20012"
                        }
                    ]
                },
                "Timestamp": 1756892217
            },
            {
                "EventType": "StaffMute",
                "StaffEventDetail": {
                    "Staffs": [
                        {
                            "Mail": "foo@tencent.com",
                            "StaffNumber": "20012"
                        }
                    ]
                },
                "Timestamp": 1756892220
            },
            {
                "EventType": "StaffUnmute",
                "StaffEventDetail": {
                    "Staffs": [
                        {
                            "Mail": "foo@tencent.com",
                            "StaffNumber": "20012"
                        }
                    ]
                },
                "Timestamp": 1756892224
            }
        ],
        "HungUpSide": "user",
        "IVRKeyPressed": [],
        "PostIVRKeyPressed": [],
        "QueuedSkillGroupId": 0,
        "QueuedSkillGroupName": "",
        "QueuedTimestamp": 0,
        "RecordURL": "https://tccc.*****d.*o***cccadmin/get**cor**PE*******23VpLFHvMi**s*n8Pnq1nmySYb***tljzGXyrb6jDk+*%***6Mhh**tOB*brQBAg==*k-***P3WIlGp******W**EkQ==-k-n***d**4**************mvk********MPYpb9zwZc4bsUdV*=*ey*********************icG*yOG1Na******************************************************************************************************************************************************************************************************************************************TVj**VH*5**********ErL2ZHYXp***p****yc****VJ***R*STNQazJ**0*P****Z*****N******X*PU1hh*U*******VRTR******lTHowcmtTM***SVVRIiwibm9uY2U**iJvVlBmQW9y*****D*wWEZTIn0=/*00-25295337***1**6*-***9*****656498**2f**72d***f1954-*00-175689232*****",
        "RequestId": "d6053004-779e-4cea-bbff-aa689b5fb9ff",
        "RingTimestamp": 1756892201,
        "ServeParticipants": [
            {
                "AcceptTimestamp": 1756892204,
                "CustomRecordURL": "https://example******p*****gzhou.tencent****************************************a76adc6-e70c-459d-8**1*5*c8*d******.mp3",
                "EndStatusString": "ok",
                "EndedTimestamp": 1756892230,
                "Mail": "foo@tencent.com",
                "Phone": "",
                "RecordId": "8a76adc6-e70c-459d-8921-56c88d91f840",
                "RecordURL": "https://tccc.**loud.com/tcccadmin/getRecord/PE**J4mQ723VpLFHvMinns4n8Pnq1nmyS****7tljzG*********I**F*e*z*gZ******+Fd6MhhwvtOBG****Ag==-k-fKVP3WIlGpg8m9*****E*************24T8YIk*s*Uj*e*************MPYpb9z***********F**dVM****Kd1DLNvTC8************s4***eA*************************************************************************************************************************************************************************************************************************************************************SUsvcDZ0QmlLV08xLzFCOW9RNXZ*bk1*ZmpzYXViem1Zb05RengvL1VuMERX*m9***NLby9RYzdLejhjVEtqZGE5dGtSVlJ**1hGZU***************U**d****DNaQjMxMl****NaIiwibm9uY2UiOi****NxbU5teG1mcjVF***********0**9891***********************94582a61****2*************1756892101.mp3",
                "RingTimestamp": 1756892198,
                "Sequence": 0,
                "SkillGroupId": 2522,
                "SkillGroupName": "foo-tel",
                "StartTimestamp": 1756892198,
                "TransferFrom": "",
                "TransferFromType": "",
                "TransferTo": "",
                "TransferToType": "",
                "Type": "staffSeat"
            }
        ],
        "StaffUserId": "foo@tencent.com",
        "StartTimeStamp": 1756892198,
        "UUI": "",
        "VoicemailAsrURL": [],
        "VoicemailRecordURL": []
    }
}
```

