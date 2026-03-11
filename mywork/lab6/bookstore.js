// Task 2: use database
// <paste your use bookstore>
use bookstore;

// Task 3: insert first author
// <paste your insertOne>

db.authors.insertOne({
    "name": "Jane Austen",
    "nationality": "British",
    "bio": {
      "short": "English novelist known for novels about the British landed gentry.",
      "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
    }
  });


// Task 4: update to add birthday
// <paste your updateOne>
db.authors.updateOne(
    { "name": "Jane Austen"},
    { $set: {"birthday": "1775-12-16"}}
);

// Task 5: insert four more authors
// <paste your insertMany or insertOne x4>
db.authors.insertMany([
    {
        "name": "Gonzalo de Berceo",
        "nationality": "Spanish",
        "birthday": "1197-01-01",
        "bio": {
          "short": "Medieval Spanish poet known for his religous works",
          "long": "Gonzalo de Berceo was a Spanish poet during the early 13th Century in the Iberica Penisula. He is mainly known for his religous focused works like Milagros de Nuestra Señora, San Millán de la Cogolla, and other Catholic religous poems"
        }
    },
    {
        "name": "Stephen King",
        "nationality": "American",
        "birthday": "1947-09-21",
        "bio": {
          "short": "Contempory American author known for his horror books",
          "long": "Stephen King is an American auther currently. He is mainly known for his horror-themed and creative story lines with many popular movie adaptaions while also having sentimental books as well. Like It, It Chapter Two, The Shining, The Green Mile, and The Shawshank Redemption."
        }
    },
    {
        "name": "Haruki Murakami",
        "nationality": "Japanese",
        "birthday": "1949-01-12",
        "bio": {
          "short": "Japanese author known for surreal, introspective fiction.",
          "long": "Haruki Murakami is a Japanese novelist whose works such as Norwegian Wood and Kafka on the Shore blend surrealism with everyday life. His writing draws on Western influences while exploring themes of loneliness, memory, and identity."
        }
    },
    {
        "name": "Leo Tolstoy",
        "nationality": "Russian",
        "birthday": "1828-09-09",
        "bio": {
            "short": "Russian novelist regarded as one of the greatest authors of all time.",
            "long": "Leo Tolstoy was a Russian novelist best known for War and Peace and Anna Karenina. His works explore themes of morality, faith, and the human condition, and he is widely considered one of the greatest writers in the history of literature."
        }
    }
])

// Task 6: total count
// <paste your countDocuments>
db.authors.countDocuments()
//Output was "5"


// Task 7: British authors, sorted by name
// <paste your find + sort>
db.authors.find({ "nationality": "British"}).sort({"name": 1})
/*output was 
[
  {
    _id: ObjectId('69b1c4ec5c7c47be58bf2088'),
    name: 'Jane Austen',
    nationality: 'British',
    bio: {
      short: 'English novelist known for novels about the British landed gentry.',
      long: 'Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development.'
    },
    birthday: '1775-12-16'
  }
]
*/