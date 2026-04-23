window.AttendanceApp = window.AttendanceApp || {
    getApiBase() {
        if (window.ATTENDANCE_API_BASE) {
            return window.ATTENDANCE_API_BASE.replace(/\/$/, "");
        }

        const savedBase = localStorage.getItem("attendanceApiBase");
        if (savedBase) {
            return savedBase.replace(/\/$/, "");
        }

        const { protocol, hostname, port, origin } = window.location;
        if ((hostname === "127.0.0.1" || hostname === "localhost") && port && port !== "8000") {
            return `${protocol}//${hostname}:8000`;
        }

        if (origin && origin.startsWith("http") && !hostname.includes("github.io")) {
            return origin;
        }

        return "http://localhost:8000";
    },

    async readJsonResponse(response) {
        const text = await response.text();
        if (!text) {
            return {};
        }

        try {
            return JSON.parse(text);
        } catch (error) {
            throw new Error("Server se valid response nahi mila.");
        }
    }
};
