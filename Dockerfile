FROM ruby:2.7
WORKDIR /app
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g yarn
COPY Gemfile Gemfile.lock ./
RUN gem install oga

RUN gem install bundler -v 2.4
RUN gem install pkg-config
RUN bundle install
COPY package.json yarn.lock ./

RUN yarn install --check-files

COPY . .

EXPOSE 3000
CMD [ "rails", "s","-b","0.0.0.0"]
