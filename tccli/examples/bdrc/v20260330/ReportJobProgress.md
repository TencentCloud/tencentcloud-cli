**Example 1: 上报任务进度**



Input: 

```
tccli bdrc ReportJobProgress --cli-unfold-argument  \
    --JobID j-20260609033851-046bf895 \
    --Progress 100 \
    --Status SUCCESS \
    --ResultData {"command": "backup", "current_phase": "archive", "error": {"code": null, "fatal": false, "message": null}, "error_count": 0, "exit_code": 0, "if_dryrun": false, "if_precheck_fs_space": false, "message_count": 0, "message_file": "/usr/local/br-agent/log/job/j-20260609033851-046bf895.json.messages", "message_truncated": false, "phases": {"archive": {"bytes_done": 1048576000, "bytes_total": 1048576000, "dirs_done": 2, "dirs_total": 2, "fail_reasons": null, "files_done": 1, "files_failed": 0, "files_skipped": 0, "files_total": 1, "finished_at": "2026-06-09T11:39:31.172782557+08:00", "percent_done": 100, "regular_files_done": 1, "regular_files_total": 1, "seconds_elapsed": 7, "seconds_remaining": 0, "skip_fail_report_local_path": null, "skip_reasons": null, "special_nodes_done": 0, "special_nodes_total": 0, "started_at": "2026-06-09T11:39:28.235533328+08:00", "status": "completed"}, "load_index": {"finished_at": "2026-06-09T11:39:28.235533128+08:00", "indexes_processed": 63, "indexes_total": 63, "started_at": "2026-06-09T11:39:23.392369334+08:00", "status": "completed"}, "scan": {"dirs_total": 2, "finished_at": "2026-06-09T11:39:28.243979471+08:00", "regular_files_total": 1, "special_nodes_total": 0, "started_at": "2026-06-09T11:39:28.235533248+08:00", "status": "completed", "total_bytes": 1048576000, "total_files": 1}}, "pid": 1104998, "runtime_params": {"backend_connections": null, "gogc": 20, "gomemlimit_mib": 136, "maxprocs": 1, "mem_level": 0, "read_concurrency": 2, "restore_workers": null}, "status": "completed", "status_file_updated_at": "2026-06-09T11:39:31.582899731+08:00", "summary": {"data_added": 0, "data_added_packed": 0, "data_blobs": 0, "dirs_changed": 1, "dirs_new": 0, "dirs_unmodified": 1, "fail_reasons": null, "files_changed": 0, "files_failed": 0, "files_new": 0, "files_skipped": 0, "files_unmodified": 1, "non_exist_source_count": 0, "non_exist_source_paths": [], "parent_snapshot_id": "50492b0d", "skip_fail_report_backend_path": "skip_fail_reports/9ebf7f0021b7edf18fad720a3be683e9da821b0125dcec04cca90837af063f7c-backup.csv", "skip_fail_report_local_path": null, "skip_reasons": null, "snapshot_id": "9ebf7f00", "special_nodes_changed": 0, "special_nodes_new": 0, "special_nodes_unmodified": 0, "total_bytes_processed": 1048576000, "total_dirs_processed": 2, "total_duration": 7.780412384, "total_files_processed": 1, "total_regular_files_processed": 1, "total_special_nodes_processed": 0, "tree_blobs": 1, "tree_size": 365, "tree_size_in_repo": 292}, "task_finished_at": "2026-06-09T11:39:31.172782687+08:00", "task_id": "j-20260609033851-046bf895", "task_started_at": "2026-06-09T11:39:23.390964146+08:00", "warning_count": 0} \
    --InstanceId br-agent-fdd97cb8-6742-b025-09e7-48721fabf789 \
    --CvmInstanceId ins-fcs3wf2c \
    --AgentStatus SUCCESS
```

Output: 
```
{
    "Response": {
        "JobID": "j-20260609033851-046bf895",
        "JobProgress": 100,
        "JobStatus": "SUCCESS",
        "Updated": true,
        "RequestId": "a290b0d8-6814-4f9a-9b97-543921b01e9e"
    }
}
```

