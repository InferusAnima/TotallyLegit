import React, { useEffect } from "react";
import { useState } from "react";
import { View, Button, Image, Text } from "react-native";
import { TailwindProvider } from "tailwindcss-react-native";
import * as ImagePicker from "expo-image-picker";
import axios from "axios";

export default function App() {
  const [image, setImage] = useState(null);
  const [data, setData] = useState(null);

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.All,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    console.log(result);
    axios
      .post("http://172.16.18.222:2898/upload", { file: result.uri })
      .then((response) => {
        const dat = `Type: ${response.data.type} - Value: ${response.data.max}\nValues: ${response.data.output}`;
        setData(dat);
      });

    if (!result.cancelled) {
      setImage(result.uri);
    }
  };

  return (
    <TailwindProvider>
      <View className="flex-1 items-center justify-center bg-white dark:bg-slate-800 transition-all">
        <Button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          title="Upload"
          onPress={pickImage}
        />
        {image && (
          <Image source={{ uri: image }} style={{ width: 200, height: 200 }} />
        )}
        {data && <Text className="text-slate-900 dark:text-white mt-5 text-base font-medium tracking-tight">{data}</Text>}
      </View>
    </TailwindProvider>
  );
}
