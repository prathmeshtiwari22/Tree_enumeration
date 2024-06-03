import React from "react";
import { StyleSheet, Text, View, Image } from "react-native";
import MapView, { Marker } from "react-native-maps";

const Plant = () => {
  return (
    <View style={{ flex: 1, marginTop: 50, backgroundColor: "#76ff7a" }}>
      <View
        style={{
          backgroundColor: "white",
          margin: 10,
          borderRadius: 6,
          padding: 10,
        }}
      >
        <Text style={{ textAlign: "center", fontSize: 15 }}>
          Order has been Approved
        </Text>

        <Text style={{ textAlign: "center", fontWeight: "bold" }}>
          Plants in 1 Hours
        </Text>
      </View>
      <View
        style={{
          alignItems: "center",
          justifyContent: "center",
          height: 500,
          width: 400,
        }}
      >
        <MapView
          style={{ height: 500, width: 400 }}
          initialRegion={{
            latitude: 19.3907, // Vasai, Mumbai latitude
            longitude: 72.8397, // Vasai, Mumbai longitude
            latitudeDelta: 0.0922,
            longitudeDelta: 0.0421,
          }}
        >
          <Marker
            coordinate={{ latitude: 19.3907, longitude: 72.8397 }} // Vasai, Mumbai coordinates
          />
        </MapView>
      </View>
      <View
        style={{
          padding: 10,
          flexDirection: "row",
          alignItems: "center",
          backgroundColor: "white",
          margin: 10,
          borderRadius: 8,
          marginTop: 10,
        }}
      >
        <Image
          style={{
            width: 60,
            height: 60,
            borderRadius: 30,
            borderColor: "#fff0f5",
            borderWidth: 1,
          }}
          source={{
            uri: "https://torontotreeremoval.ninja/wp-content/uploads/plant-a-tree-toronto.jpg",
          }}
        />
        <View style={{ marginLeft: 20 }}>
          <Text style={{ fontSize: 18, fontWeight: "700", color: "#ff6e4a" }}>
            189 Plants Near Your Location
          </Text>
          <Text style={{ fontSize: 17, fontWeight: "600", color: "#696969" }}>
            Anyone will pick your order
          </Text>
        </View>
      </View>
    </View>
  );
};

export default Plant;

const styles = StyleSheet.create({});
