import { createDrawerNavigator, DrawerContentScrollView, DrawerItem, DrawerItemList } from "@react-navigation/drawer";
import { NavigationContainer } from "@react-navigation/native";
import { ActivityIndicator } from "react-native";
import { useEffect, useState } from "react/cjs/react.production.min";
import Home from "./components/Home/Home";
import Login from "./components/User/Login";
import API, { endpoints } from "./configs/API";
import React, { useReducer } from 'react'
import Lesson from "./components/Lesson/Lesson";
import LessonDetails from "./components/Lesson/LessonDetails";
import MyContext from "./configs/MyContext";
import MyUserReducer from "./reducers/MyUserReducer";
import Logout from "./components/User/Logout";
import Register from "./components/User/Register";


const App = () => {

}

const MyDrawerItem = (props) => {

}

export default App;



// export default function App() {
//   return (
//     <View style={styles.container}>
//       <Text>Open up App.js to start working on your app!</Text>
//       <StatusBar style="auto" />
//     </View>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',
//     justifyContent: 'center',
//   },
// });
