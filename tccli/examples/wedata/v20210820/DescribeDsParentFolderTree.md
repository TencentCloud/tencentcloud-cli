**Example 1: 查询父目录树**

编排空间 用于定位工作流、任务

Input: 

```
tccli wedata DescribeDsParentFolderTree --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20250812172427822 \
    --NewFolderTreeMode True
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Children": [
                    {
                        "Children": [],
                        "Id": "088f6591-1339-4473-8cda-18e43518a6df",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjpmYWxzZSwib3duZXJJZCI6IjEwMDAzNjg4NTk3OCIsIndvcmtmbG93RGVzYyI6IiJ9",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "2321R2",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "0500be1e-ad14-487f-a695-ac5b51982be4",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjpmYWxzZSwib3duZXJJZCI6IjEwMDAzNjg4NTk3OCIsIndvcmtmbG93RGVzYyI6IiJ9",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "alarm_zd10",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "53897748-8595-477d-9a23-5d28caba3a30",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDM2ODg1OTc4Iiwid29ya2Zsb3dEZXNjIjoiIn0=",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "apitest",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "09f8f989-98e6-49d3-a4c2-ec5a8a1729cc",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDM2ODg1OTc4Iiwid29ya2Zsb3dEZXNjIjoiIn0=",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "apitestworkflow",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "ada4318d-1a40-45e8-8936-7798d9d21d1a",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDM2ODg1OTc4Iiwid29ya2Zsb3dEZXNjIjoiIn0=",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "crontab",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "190751a2-be18-40c5-900a-51c1c4defd62",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDM2ODg1OTc4OzEwMDAyODY5NDI2NiIsIndvcmtmbG93RGVzYyI6IiJ9",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "makeworkflow",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "36471aa7-7f80-465b-8ad1-f338b0817659",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDM2ODg1OTc4Iiwid29ya2Zsb3dEZXNjIjoiIn0=",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "makeworkflow_order",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "5b14d1ee-68ef-42b1-9614-ab93acbcddc1",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoibWFudWFsIiwic3VibWl0RmxhZyI6ZmFsc2UsIm93bmVySWQiOiIxMDAwMzY4ODU5NzgiLCJ3b3JrZmxvd0Rlc2MiOiIifQ==",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "manual_trigger",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "8e2f185b-cfa5-4c7e-b9de-445ef23d7e76",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoibWFudWFsIiwic3VibWl0RmxhZyI6ZmFsc2UsIm93bmVySWQiOiIxMDAwMzY4ODU5NzgiLCJ3b3JrZmxvd0Rlc2MiOiIifQ==",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "manual_trigger22",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "e62f65cd-4674-40a3-800f-7bfaa5a51a96",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjpmYWxzZSwib3duZXJJZCI6IjEwMDAzNjg4NTk3OCIsIndvcmtmbG93RGVzYyI6IiJ9",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "redo",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "be72409a-4430-4089-978a-26beac31f22e",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjpmYWxzZSwib3duZXJJZCI6IjEwMDAzNjg4NTk3OCIsIndvcmtmbG93RGVzYyI6IiJ9",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "selfworkflowcycle",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "05239aaa-325b-4d12-9c86-db4358ef64ce",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDM2ODg1OTc4Iiwid29ya2Zsb3dEZXNjIjoiIn0=",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "test12234",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "30c4dd45-e9d7-11ef-8ec8-b8599f277de5",
                        "IsLeaf": false,
                        "Params": null,
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "timezone",
                        "Type": "folder"
                    },
                    {
                        "Children": [],
                        "Id": "b32c7cdd-d5be-456b-996d-07ffb59f968d",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjpmYWxzZSwib3duZXJJZCI6IjEwMDAzNjg4NTk3OCIsIndvcmtmbG93RGVzYyI6IiJ9",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "xR2",
                        "Type": "workflow"
                    },
                    {
                        "Children": [
                            {
                                "Children": [],
                                "Id": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_ETL",
                                "IsLeaf": false,
                                "Params": "eyJ0YXNrTm9kZUVudW0iOiJFVEwiLCJ0YXNrTm9kZVNvcnQiOjF9",
                                "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c",
                                "Title": "数据集成",
                                "Type": "taskNode"
                            },
                            {
                                "Children": [],
                                "Id": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_EMR",
                                "IsLeaf": false,
                                "Params": "eyJ0YXNrTm9kZUVudW0iOiJFTVIiLCJ0YXNrTm9kZVNvcnQiOjJ9",
                                "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c",
                                "Title": "EMR",
                                "Type": "taskNode"
                            },
                            {
                                "Children": [],
                                "Id": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_DLC",
                                "IsLeaf": false,
                                "Params": "eyJ0YXNrTm9kZUVudW0iOiJETEMiLCJ0YXNrTm9kZVNvcnQiOjN9",
                                "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c",
                                "Title": "DLC",
                                "Type": "taskNode"
                            },
                            {
                                "Children": [],
                                "Id": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_TDSQL",
                                "IsLeaf": false,
                                "Params": "eyJ0YXNrTm9kZUVudW0iOiJURFNRTCIsInRhc2tOb2RlU29ydCI6NH0=",
                                "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c",
                                "Title": "TDSQL",
                                "Type": "taskNode"
                            },
                            {
                                "Children": [],
                                "Id": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_TCHOUSE",
                                "IsLeaf": false,
                                "Params": "eyJ0YXNrTm9kZUVudW0iOiJUQ0hPVVNFIiwidGFza05vZGVTb3J0Ijo1fQ==",
                                "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c",
                                "Title": "TCHOUSE",
                                "Type": "taskNode"
                            },
                            {
                                "Children": [
                                    {
                                        "Children": null,
                                        "Id": "20250702193131192",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDctMDQgMTA6MjM6MjMiLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJPIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "alarm_task_avg_test",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250701113257754",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDctMDEgMTE6NTI6MzYiLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJPIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "alarm_task_test1",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250701163709601",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0IjpmYWxzZSwidXBkYXRlVXNlcklkIjoiMTAwMDM2ODg1OTc4IiwidmlydHVhbFRhc2tJZCI6bnVsbCwicmVmZXJlbmNlVGVtcGxhdGUiOmZhbHNlLCJidW5kbGVJZCI6bnVsbCwidXBkYXRlVXNlciI6ImNhcmxzaGkiLCJ2aXJ0dWFsRmxhZyI6ZmFsc2UsInVwZGF0ZVRpbWUiOiIyMDI1LTA4LTAxIDE3OjAyOjQyIiwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJwcm9qZWN0SWQiOiIxNDYwOTQ3ODc4OTQ0NTY3Mjk2Iiwic3RhdHVzIjoiTyJ9",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "alarm_task_wait_test",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250708114505208",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDctMDggMTc6NTQ6MzQiLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJZIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "day_father",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250731113934238",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0IjpmYWxzZSwidXBkYXRlVXNlcklkIjoiMTAwMDM2ODg1OTc4IiwidmlydHVhbFRhc2tJZCI6bnVsbCwicmVmZXJlbmNlVGVtcGxhdGUiOmZhbHNlLCJidW5kbGVJZCI6bnVsbCwidXBkYXRlVXNlciI6ImNhcmxzaGkiLCJ2aXJ0dWFsRmxhZyI6ZmFsc2UsInVwZGF0ZVRpbWUiOiIyMDI1LTA3LTMxIDExOjQxOjM5Iiwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJwcm9qZWN0SWQiOiIxNDYwOTQ3ODc4OTQ0NTY3Mjk2Iiwic3RhdHVzIjoiTiJ9",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "hour_up_minite_notify",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250731165042620",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDctMzEgMTY6NTE6NDAiLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJZIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "notify_day_father_1",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250731164955054",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0IjpmYWxzZSwidXBkYXRlVXNlcklkIjoiMTAwMDM2ODg1OTc4IiwidmlydHVhbFRhc2tJZCI6bnVsbCwicmVmZXJlbmNlVGVtcGxhdGUiOmZhbHNlLCJidW5kbGVJZCI6bnVsbCwidXBkYXRlVXNlciI6ImNhcmxzaGkiLCJ2aXJ0dWFsRmxhZyI6ZmFsc2UsInVwZGF0ZVRpbWUiOiIyMDI1LTA3LTMxIDE2OjQ5OjU0Iiwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJwcm9qZWN0SWQiOiIxNDYwOTQ3ODc4OTQ0NTY3Mjk2Iiwic3RhdHVzIjoiTiJ9",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "notify_minute_son_1",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250630162948606",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoid2VuamlleWFvIiwidmlydHVhbEZsYWciOmZhbHNlLCJ1cGRhdGVUaW1lIjoiMjAyNS0wOC0xMiAxNjoyMTo1OCIsIndvcmtmbG93VHlwZSI6ImN5Y2xlIiwicHJvamVjdElkIjoiMTQ2MDk0Nzg3ODk0NDU2NzI5NiIsInN0YXR1cyI6IkYifQ==",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "quality_timezone",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250708114842380",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDctMDkgMTQ6MzI6NDciLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJZIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "son_hour",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250718153727550",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDctMTggMTU6NDA6MjAiLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJGIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "timezone_minute",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250812172427822",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDgtMTIgMTc6Mjg6MzUiLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJZIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "tz7_day_test1",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250812172235381",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDgtMTIgMTc6MjM6NTAiLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJZIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "tz8_day_test1",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250812151805859",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDgtMTIgMTU6MTg6MzUiLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJZIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "tz8_task_test1",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250703141701601",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDgtMDEgMTg6MzA6MzgiLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJZIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "tz_task_test1",
                                        "Type": "task"
                                    },
                                    {
                                        "Children": null,
                                        "Id": "20250707101602108",
                                        "IsLeaf": true,
                                        "Params": "eyJ0YXNrVHlwZUlkIjozNSwic3VibWl0Ijp0cnVlLCJ1cGRhdGVVc2VySWQiOiIxMDAwMzY4ODU5NzgiLCJ2aXJ0dWFsVGFza0lkIjpudWxsLCJyZWZlcmVuY2VUZW1wbGF0ZSI6ZmFsc2UsImJ1bmRsZUlkIjpudWxsLCJ1cGRhdGVVc2VyIjoiY2FybHNoaSIsInZpcnR1YWxGbGFnIjpmYWxzZSwidXBkYXRlVGltZSI6IjIwMjUtMDctMzEgMTE6MTM6NTEiLCJ3b3JrZmxvd1R5cGUiOiJjeWNsZSIsInByb2plY3RJZCI6IjE0NjA5NDc4Nzg5NDQ1NjcyOTYiLCJzdGF0dXMiOiJZIn0=",
                                        "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                        "Title": "tz_task_test2",
                                        "Type": "task"
                                    }
                                ],
                                "Id": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_GENERAL",
                                "IsLeaf": false,
                                "Params": "eyJ0YXNrTm9kZUVudW0iOiJHRU5FUkFMIiwidGFza05vZGVTb3J0Ijo2fQ==",
                                "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c",
                                "Title": "通用",
                                "Type": "taskNode"
                            },
                            {
                                "Children": [],
                                "Id": "b8f62e8b-5484-4810-aff7-3815e5abcb0c_ACROSS_WORKFLOWS",
                                "IsLeaf": false,
                                "Params": "eyJ0YXNrTm9kZUVudW0iOiJBQ1JPU1NfV09SS0ZMT1dTIiwidGFza05vZGVTb3J0Ijo4fQ==",
                                "ParentId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c",
                                "Title": "跨工作流",
                                "Type": "taskNode"
                            }
                        ],
                        "Id": "b8f62e8b-5484-4810-aff7-3815e5abcb0c",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDM2ODg1OTc4Iiwid29ya2Zsb3dEZXNjIjoiIn0=",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "zd10",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "0a38dea4-a0dd-4f05-be94-945e1bf8d17c",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjpmYWxzZSwib3duZXJJZCI6IjEwMDAzNjg4NTk3OCIsIndvcmtmbG93RGVzYyI6IiJ9",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "zhengda35",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "1dd4e41f-af96-4114-b148-de2ebcbaeb9e",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDM2ODg1OTc4Iiwid29ya2Zsb3dEZXNjIjoiIn0=",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "zhengda6",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "1dd3f69e-845e-42fe-876e-eab9d03eeb66",
                        "IsLeaf": false,
                        "Params": "eyJidW5kbGVJZCI6bnVsbCwid29ya2Zsb3dUeXBlIjoiY3ljbGUiLCJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDM2ODg1OTc4Iiwid29ya2Zsb3dEZXNjIjoiIn0=",
                        "ParentId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                        "Title": "zhiban",
                        "Type": "workflow"
                    }
                ],
                "Id": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                "IsLeaf": false,
                "Params": null,
                "ParentId": "",
                "Title": "carlshi",
                "Type": "folder"
            }
        ],
        "RequestId": "5f73561d-54cf-48eb-be11-b55a84920184"
    }
}
```

