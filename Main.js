import React, { useState } from "react";
import {
  StyleSheet,
  View,
  FlatList,
  Alert,
  TouchableOpacity,
  Text,
} from "react-native";
import { StatusBar } from "expo-status-bar";

import AddItem from "./components/AddItem";
import ListItem from "./components/ListItem";
import Header from "./components/Header";
import { useNavigation } from "@react-navigation/native";

const Main = () => {
   const navigation = useNavigation();
  const [items, setItems] = useState([
    { id: Math.random().toString(), text: "Coconut Tree" },
    { id: Math.random().toString(), text: "Pine Tree" },
    { id: Math.random().toString(), text: "Mango Tree" },
    { id: Math.random().toString(), text: "Oak Tree" },
    { id: Math.random().toString(), text: "Neem Tree" },
    { id: Math.random().toString(), text: "Peepal Tree" },
    { id: Math.random().toString(), text: "Tulsi" },
    { id: Math.random().toString(), text: "Aloe Vera" },
  ]);

  const deleteItem = (id) => {
    setItems((prevItems) => {
      return prevItems.filter((item) => item.id != id);
    });
  };

  const addItem = (text) => {
    if (!text) {
      Alert.alert("❗Enter item to add", " Item name cannot be empty.", [
        {
          text: "Cancel",
          style: "cancel",
        },
        { text: "OK" },
      ]);
      return;
    } else {
      setItems((prevItems) => {
        return [{ id: Math.random().toString(), text }, ...prevItems];
      });
    }
  };

  return (
    <>
      <StatusBar style="auto" />
      <View style={styles.container}>
        <Header title=" PLANTING TREE 🌱" />
        <AddItem addItem={addItem} />
        <FlatList
          data={items}
          renderItem={({ item }) => (
            <ListItem item={item} deleteItem={deleteItem} />
          )}
        />
        <TouchableOpacity
          style={styles.addButton}
          onPress={() => navigation.navigate("Order")}
        >
          <Text style={styles.addButtonText}>Plant it...</Text>
        </TouchableOpacity>
      </View>
    </>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 25,
    backgroundColor: "lightyellow",
    position: "relative",
  },
  addButton: {
    position: "absolute",
    bottom: 20,
    backgroundColor: "#7cfc00",
    borderRadius: 30,
    paddingVertical: 15,
    paddingHorizontal: 20,
    alignSelf: "center",
  },
  addButtonText: {
    color: "white",
    fontSize: 18,
    fontWeight: "bold",
  },
});

export default Main;
