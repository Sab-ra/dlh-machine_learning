# API Data Collection

## 0-passengers.py

By using the Swapi API, create a method that returns the list of ships that can hold a given number of passengers:

- [x] Prototype: `def availableShips(passengerCount)`
- [x] Don't forget the pagination
- [x] If no ship available, return an empty list.

## 1-sentience.py

By using the Swapi API, create a method that returns the list of names of the home planets of all sentient species.

- [x] Prototype: `def sentientPlanets():
- [x] Don't forget the pagination
- [x] sentient type is either in the classification or designation attributes.

## 2-user_location.py

By using the GitHub API, write a script that prints the location of a specific user:

- [x] The user is passed as first argument of the script with the full API URL, example: ./2-user_location.py https://api.github.com/users/holbertonschool
- [x] If the user doesn't exist, print Not found
- [x] If the status code is 403, print Reset in X min where X is the number of minutes from now and the value of X-Ratelimit-Reset
- [x] Your code should not be executed when the file is imported (you should use if __name__ == '__main__':)

_Tips: Playing with an API that has a Rate limit is challenging, mainly because you don't have the control on when the quota will be reset - we really encourage you to analyze the API a much as you can before coding and be able to "mock the API response"_

## 3-first_launch.py

## 3. First launch

By using the (unofficial) SpaceX API, write a script that displays the first launch with these information:

- [x] Name of the launch
- [x] The date (in local time)
- [x] The rocket name
- [x] The name (with the locality) of the launchpad

Format: `<launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)`

we encourage you to use the date_unix for sorting it - and if 2 launches have the same date, use the first one in the API result.

Your code should not be executed when the file is imported (you should use if __name__ == '__main__':)

## 4-rocket_frequency.py

