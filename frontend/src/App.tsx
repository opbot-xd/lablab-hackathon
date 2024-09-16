import { useState, useEffect } from "react";
import axios from "axios";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

interface PostResponse {
  uuid: string;
}

interface GetResponse {
  tweet: string;
  pending: boolean;
}

export default function App() {
  const [hashtag, setHashtag] = useState<string>("");
  const [mood, setMood] = useState<string>("");
  const [uuid, setUuid] = useState<string | null>(null);
  const [tweet, setTweet] = useState<string>("Waiting for tweet...");
  const [pending, setPending] = useState<boolean>(true);

  const handleFormSubmit = async () => {
    try {
      const response = await axios.post<PostResponse>("https://lablab-hackathon.onrender.com/get_data", {
        tweet: hashtag,
        mood: mood,
      });
      setUuid(response.data.uuid);
    } catch (error) {
      console.error("Error submitting the form:", error);
    }
  };

  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (uuid && pending) {
      interval = setInterval(async () => {
        try {
          const response = await axios.get<GetResponse>("https://lablab-hackathon.onrender.com/status", {
            headers: {
              uuid: uuid,
            },
          });
          setTweet(response.data.tweet || "Tweet still processing...");
          setPending(response.data.pending);
          if (!response.data.pending) {
            clearInterval(interval);
          }
        } catch (error) {
          console.error("Error fetching tweet status:", error);
        }
      }, 10000);
    }

    return () => clearInterval(interval);
  }, [uuid, pending]);

  return (
    <div className="flex gap-8 flex-col w-screen h-screen bg-gradient-to-r from-indigo-500 from-10% via-sky-500 justify-center items-center">
      <Card className="w-[350px]">
        <CardHeader>
          <CardTitle>Create your tweet</CardTitle>
          <CardDescription>Get a biased tweet in one go</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid w-full items-center gap-4">
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="hashtag">Hashtag</Label>
              <Input
                id="hashtag"
                placeholder="Put your hashtag here"
                value={hashtag}
                onChange={(e) => setHashtag(e.target.value)}
              />
            </div>
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="framework">
                Which sentiment do you want in your tweet?
              </Label>
              <Select onValueChange={(value) => setMood(value)}>
                <SelectTrigger id="framework">
                  <SelectValue placeholder="Select" />
                </SelectTrigger>
                <SelectContent position="popper">
                  <SelectItem value="Negative">Negative</SelectItem>
                  <SelectItem value="Positive">Positive</SelectItem>
                  <SelectItem value="Neutral">Neutral</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
        </CardContent>
        <CardFooter className="flex justify-center items-center">
          <Button onClick={handleFormSubmit}>Let's Go!!</Button>
        </CardFooter>
      </Card>
      <div className="rounded-xl border h-1/5 w-2/5 bg-card text-card-foreground shadow p-4">
        <Label htmlFor="tweet">{tweet}</Label>
      </div>
    </div>
  );
}
