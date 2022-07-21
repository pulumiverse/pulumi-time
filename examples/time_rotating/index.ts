import * as time from "@pulumiverse/time";

export const time_rotation = new time.TimeRotating("my-time-rotating", {
    rotationMinutes: 1,
});

export const id = time_rotation.id;
