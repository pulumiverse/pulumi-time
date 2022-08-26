import * as time from "@pulumiverse/time";

export const time_rotation = new time.Rotating("my-time-rotating", {
    rotationMinutes: 1,
});

export const id = time_rotation.id;
