import axios from "axios";

export const endpoints = {
    'destinations': '/destinations/',
    // 'trip-paths': '/trip-paths/',
    // 'login': '/o/token/',
    // 'current-user': '/users/current-user/',
    // 'register': '/users/',
}

export const authApi = (accessToken) => axios.create({
    baseURL: "http://localhost:8000/",
    headers: {
        "Authorization": `bearer ${accessToken}`
    }
})

export default axios.create({
    baseURL: "http://localhost:8000/"
})