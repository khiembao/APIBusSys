import React, { useEffect, useState } from "react"
import Style from "../User/Style";

import MyStyles from "../../styles/MyStyles";
import { ActivityIndicator, Image, Text, View } from "react-native";
import API, { endpoints } from "../../configs/API";

const Home = () => {
    const[destinations, setDestinations] = React.useState(null)

    React.useEffect(() => {
        const loadDestinations = async () => {
            try {
                let res = await API.get(endpoints['destinations']);
                setDestinations(res.data.results)
            } catch (ex) {
                console.error(ex);
                
            }

        }
        loadDestinations();
    }, []);

    return(
        <View style={MyStyles.container}>
            <Text>HOME</Text>
            {destinations===null?<ActivityIndicator/>:<>
                {destinations.map(d => (
                    <View key={d.id}>
                        <Text>{d.name}</Text>

                    </View>
                ))}
            </>}
        </View>
    );
}
export default Home;