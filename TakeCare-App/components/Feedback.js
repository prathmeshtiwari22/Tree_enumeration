import { StatusBar } from "expo-status-bar";
import React, { useEffect, useState } from "react";
import { StyleSheet, Text, TextInput, Button, View } from "react-native";
import * as MailComposer from "expo-mail-composer";
import * as Print from "expo-print";

// expo add expo-print expo-mail-composer

export default function Feedback() {
  const [isAvailable, setIsAvailable] = useState(false);
  const [recipients, setRecipients] = useState([]);
  const [subject, setSubject] = useState("");
  const [body, setBody] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    async function checkAvailability() {
      const isMailAvailable = await MailComposer.isAvailableAsync();
      setIsAvailable(isMailAvailable);
    }

    checkAvailability();
  }, []);

  const sendMail = async () => {
    if (recipients.length === 0) {
      alert("Please add recipients before sending the email.");
      return;
    }

    const { uri } = await Print.printToFileAsync({
      html: "<h1>My pdf!</h1>",
    });

    MailComposer.composeAsync({
      subject: subject,
      body: body,
      recipients: recipients,
      attachments: [uri],
    });
  };

  const addRecipient = () => {
    if (!email) {
      alert("Please enter an email address.");
      return;
    }

    setRecipients([...recipients, email]);
    setEmail("");
  };

  const showRecipients = () => {
    if (recipients.length === 0) {
      return <Text>No recipients added</Text>;
    }

    return recipients.map((recipient, index) => {
      return <Text key={index}>{recipient}</Text>;
    });
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        value={subject}
        onChangeText={setSubject}
        placeholder="Subject"
      />
      <TextInput
        style={styles.input}
        value={body}
        onChangeText={setBody}
        placeholder="Body"
        multiline={true}
        numberOfLines={4}
      />
      <TextInput
        style={styles.input}
        value={email}
        onChangeText={setEmail}
        placeholder="Email"
        keyboardType="email-address"
      />
      <Button title="Add Recipient" onPress={addRecipient} />
      {showRecipients()}
      {isAvailable ? (
        <Button title="Send Mail" onPress={sendMail} />
      ) : (
        <Text>Email not available</Text>
      )}
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
    paddingHorizontal: 20,
  },
  input: {
    width: "100%",
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
});
