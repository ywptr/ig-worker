Experimental architecture for IG, deploying queue worker on a separate project

Status: Failed
Reason: In default push mode, a deployed queue is strictly per-project only. A separate project will not have access to Vercel queue.
        It may have potential to run on poll mode, but poll mode requires a continually running process, something that will require additional and separate provisioning from Vercel. (Vercel does not provide a way to continually run persistent processes)

This repo is only for reference and is no longer updated