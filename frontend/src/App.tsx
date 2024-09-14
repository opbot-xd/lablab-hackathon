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

export default function App() {
  return (
    <div className="flex gap-8 flex-col w-screen h-screen bg-gradient-to-r from-indigo-500 from-10% via-sky-500 justify-center items-center">
      <Card className="w-[350px]">
        <CardHeader>
          <CardTitle>Create your tweet</CardTitle>
          <CardDescription>
            Get a baised tweet in one go
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form>
            <div className="grid w-full items-center gap-4">
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="hashtag">Hashtag</Label>
                <Input id="hashtag" placeholder="Put you hashtag here" />
              </div>
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="framework">Which sentiments you want in your tweet?</Label>
                <Select>
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
          </form>
        </CardContent>
        <CardFooter className="flex justify-center items-center">
          <Button>Lets Go!!</Button>
        </CardFooter>
      </Card>
      <div className="rounded-xl border h-1/5 w-2/5 bg-card text-card-foreground shadow p-4"><Label htmlFor="terms">Output soon...</Label></div>
    </div>
  );
}
