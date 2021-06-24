dice_job_spec = {
        "backoffLimit": 25,
        "completions": 3,
        "parallelism": 3,
        "template": {
            "spec": {
                "containers": [
                    {
                        "image": "kodekloud/throw-dice",
                        "name": "math-add"
                    }
                ],
                "restartPolicy": "Never"
            }
        }
}
