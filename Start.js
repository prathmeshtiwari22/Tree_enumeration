import { StatusBar } from "expo-status-bar";
import {
  StyleSheet,
  Text,
  View,
  Image,
  ScrollView,
  Button,
} from "react-native";
import { useNavigation } from "@react-navigation/native";

const Start = () => {
  const navigation = useNavigation();
  return (
    <View style={styles.container}>
      <ScrollView>
        <View style={styles.Navbar}>
          <Button
            title="Start"
            color="#008001"
            onPress={() => {
              navigation.navigate("Main");
            }}
          />
        </View>

        <View style={styles.mainbox}>
          <Image
            style={styles.Oneimage}
            source={require("./assets/maxresdefault.jpg")}
          />

          <View style={styles.BoxOne}>
            <View style={styles.Text}>
              <Text style={styles.HeadingText}>Banana Tree</Text>

              <Text style={styles.Infotext}>
                Banyan trees are mostly seen in different regions of the country
                and are the national . his huge type of tree has extensive
                branches
              </Text>
            </View>

            <Image
              style={styles.InsideImage}
              source={require("./assets/bana.jpg")}
            />
          </View>

          <View style={styles.BoxOne}>
            <View style={styles.Text}>
              <Text style={styles.HeadingText}>Neem Tree</Text>

              <Text style={styles.Infotext}>
                The most common and popular tree of probably every household is
                the neem tree that has bright leaves and goes up to the height
                of 100 feet.
              </Text>
            </View>

            <Image
              style={styles.InsideImage}
              source={require("./assets/neemtree.jpg")}
            />
          </View>

          <View style={styles.BoxOne}>
            <View style={styles.Text}>
              <Text style={styles.HeadingText}>Peepal Tree</Text>

              <Text style={styles.Infotext}>
                It is a fast-growing tree having heart-shaped leaves with a
                large crown. It sheds its leaves in the month of March and
                April.
              </Text>
            </View>

            <Image
              style={styles.InsideImage}
              source={require("./assets/peelpaltree.jpg")}
            />
          </View>

          <View style={styles.BoxOne}>
            <View style={styles.Text}>
              <Text style={styles.HeadingText}> Aloe VeraTree</Text>

              <Text style={styles.Infotext}>
                It is a fast-growing tree having heart-shaped leaves with a
                large crown. It sheds its leaves in the month of March and
                April.
              </Text>
            </View>

            <Image
              style={styles.InsideImage}
              source={require("./assets/peelpaltree.jpg")}
            />
          </View>

          <View style={styles.BoxOne}>
            <View style={styles.Text}>
              <Text style={styles.HeadingText}> Tulsi Tree</Text>

              <Text style={styles.Infotext}>
                Tulsi plant is considered as a holy and religious plant in
                India. Height reaches about 75 cm to 90 cm. The leaves are round
                oval shaped which contain essential oils.
              </Text>
            </View>

            <Image
              style={styles.InsideImage}
              source={require("./assets/peelpaltree.jpg")}
            />
          </View>
          <View style={styles.BoxOne}>
            <View style={styles.Text}>
              <Text style={styles.HeadingText}> Coconut Tree</Text>

              <Text style={styles.Infotext}>
                The coconut is known for its versatility and is often called the
                "tree of life." It provides food, drink, shelter, and various
                materials for everyday use in many tropical regions.
              </Text>
            </View>

            <Image
              style={styles.InsideImage}
              source={require("./assets/coco.jpeg")}
            />
          </View>
          <View style={styles.BoxOne}>
            <View style={styles.Text}>
              <Text style={styles.HeadingText}> Mango Tree </Text>

              <Text style={styles.Infotext}>
                Mango trees are renowned for their delicious fruit, which is
                enjoyed worldwide. They are native to South Asia but are now
                cultivated in many tropical and subtropical regions.
              </Text>
            </View>

            <Image
              style={styles.InsideImage}
              source={require("./assets/mango.jpeg")}
            />
          </View>
          <View style={styles.BoxOne}>
            <View style={styles.Text}>
              <Text style={styles.HeadingText}> Oak Tree </Text>

              <Text style={styles.Infotext}>
                Oak trees are known for their strength and longevity. They are
                commonly found in temperate forests and, which is used in
                construction and furniture making.
              </Text>
            </View>

            <Image
              style={styles.InsideImage}
              source={require("./assets/oak.jpeg")}
            />
          </View>
          <View style={styles.BoxOne}>
            <View style={styles.Text}>
              <Text style={styles.HeadingText}> Pine Tree </Text>

              <Text style={styles.Infotext}>
                Pine trees are evergreen conifers that are found in many parts
                of the world,colder climates. They are known for
                their tall stature, needle-like leaves, and pine cones.
              </Text>
            </View>

            <Image
              style={styles.InsideImage}
              source={require("./assets/Eastern-White-Pine-Tree.jpg")}
            />
          </View>
        </View>

        <Text style={styles.HeadingOnecen} onPress={()=> navigation.navigate("Feedback")}>Our Section</Text>

        <View style={styles.Boxing}>
          <Image
            style={styles.infoimage}
            source={require("./assets/donatetow.jpg")}
          />

          <Image
            style={styles.infoimage}
            source={require("./assets/cup.jpg")}
          />
        </View>
      </ScrollView>

      <StatusBar style="auto" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#e8e8e8",
  },

  Navbar: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-around",
    width: "100%",
    height: 60,
    backgroundColor: "#008000",
    marginTop: 35,
  },

  Oneimage: {
    width: "80%",
    height: 150,
    marginTop: 30,
    borderRadius: 10,
  },

  mainbox: {
    flexDirection: "column",
    alignItems: "center",
  },

  BoxOne: {
    width: "90%",
    height: 150,
    backgroundColor: "#fff",
    marginTop: 40,
    borderRadius: 10,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-around",
    padding: 2,
  },

  InsideImage: {
    width: "30%",
    height: 120,
    borderRadius: 6,
  },

  Text: {
    flexDirection: "column",
    width: "60%",
    height: 130,
    padding: 4,
  },

  HeadingText: {
    fontWeight: "bold",
    fontSize: 20,
  },

  Infotext: {
    marginTop: 5,
  },

  Boxing: {
    width: "100%",
    height: 170,
    marginTop: 10,
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
  },

  HeadingOnecen: {
    fontWeight: "bold",
    fontSize: 20,
    textAlign: "center",
    marginTop: 40,
  },

  infoimage: {
    width: "35%",
    height: 130,
    backgroundColor: "#333",
    borderRadius: 5,
  },
});
export default Start;
