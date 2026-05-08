---
title: Build Your Personal Website for Free Using React.js
date: '2024-10-01T14:59:32+00:00'
draft: false
tags:
- Blog
- Coding
- Javascript
url: /blog/article/build-your-personal-website-free-reactjs
cover:
  image: /images/build-your-personal-website-for-free-using-reactjs/article1-main.webp
  alt: Build Your Personal Website for Free Using React.js
  relative: false
---

* [**[Original Article]**](https://medium.com/better-programming/get-your-personal-website-for-free-create-it-with-reactjs-b7e3c3c874b4)

In this article, I want to show you how to create your personal website for free!

To get that, we are going to use [GitHub Pages](https://pages.github.com/) which will allow us to host our website and even will give us a secure (HTTPS) URL.

Optionally, we can even use our own domain name, in such case, it is the only thing that you will need to pay for.

As the title says, we want to create the website using ReactJs.

Why?

Well, you can create it more simply, by following the recommendations from GitHub Pages. You can even get a website template with mock data that you can change!

But, as a software developer who knows something about ReactJs, I wanted to create a custom personal page, which I can change in the future, use the UI controls and library that I want, or whatever. Maybe doing this is a bit more difficult but I think it is the price to pay to get customization.

Finally, I used [MaterialUI](https://mui.com/material-ui/) and [NextJs](https://nextjs.org/) libraries. I will explain why later.

## **GitHub Pages**

![](/images/build-your-personal-website-for-free-using-reactjs/1*bju7hnLuJhkUAKfVCsaF_g.gif)

GitHub Pages is a service that GitHub gives developers for free to create personal or company websites. You only need a GitHub user and then create a GitHub repository named `<yourGithubUsername>.github.io` . After that, you commit and push a file `index.html` to your repo, and that is it. You will have your site working (maybe it takes some minutes). You are able to check it at `https://<yourGitHubUsername>.github.io` .

As we can render static web pages ([GitHub pages suggest](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll) using [Jekyll](https://jekyllrb.com/) to generate your site) I decided to use [NextJs](https://nextjs.org/) in order to create my ReactJs app. Next.js allows ReactJs server-side rendering, but also, it generates a static web app that we can just copy into the github.io repo and push it.

## **Why Next.js?**

We can use ReactJs to create Single Page Applications (SPAs), it has a route library (react-routes) which we can use to create multiple pages and more complex and complete applications in general. The problem is that we will need a Node.js app where to host it. That is why we decided to use NextJs.

Next.js allows us to do server-side rendering, which is just creating the webpage before sending it to the browser and then adding ReactJs and the rest of the javascript code. This is very useful in terms of SEO. But also, NextJs build and export a static website, and we can just copy and paste it into your GitHub Page, which will work.

My goal in creating my personal web is to create a functional and customizable web in React, but not to use the purest react best practices, like using redux, react-routes, getting the data from APIs endpoints, or using GraphQL… That is why I get the data from static files and I don’t care about unit tests and so on.

## **Let’s create our GitHub Pages repository**

As mentioned before, we need to create a new project with this pattern `<yourGitHubUsername>.github.io` , so, in my case, the repo name is `rulyotano.github.io` . After that, you may clone your repo into your local machine and create an `index.html` file with some content. After pushing the changes to GitHub, you should see something in `https://<yourGitHubUsername>.github.io` , it may take some seconds.

Here on this point, it is good for you to know that you can use [Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll#about-jekyll) to [generate your website](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll). It is the recommended option from GitHub Pages. They describe it like this:

> *Jekyll is a static site generator with built-in support for GitHub Pages and a simplified build process. Jekyll takes Markdown and HTML files and creates a complete static website based on your choice of layouts. Jekyll supports Markdown and Liquid, a templating language that loads dynamic content on your site.*

If you don’t want to use Jekyll you are free to create your own static web. That is basically what we are going to do here.

Another important thing here is that you can [enable HTTPS on your website](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), but also, you can also use [your custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages). I recommend following the guides as they are pretty well explained. Basically, you will need to go to your GitHub repository -> Settings tab -> Pages (under the Code and Automation section). Here you can configure both. Also, you will probably need to add some records to your domain provider configuration, and in order to verify you own this website, you will need to include a CNAME file in your code with your domain name as a value.

## **Let’s create our Website project and repository**

We don’t need to create another repository for this project. We can directly update our GitHub Pages repo, but since we are going to create a Next.js + React.js project, it needs to be built and released, and the output is what we can copy into our Pages repo. If we don't create this repo, we can’t update our website later, or at least we will have to do it directly in the output and will lose ReactJs benefits.

First, we need to create the new GitHub repository, the name doesn’t matter. I just named it [mui-profile](https://github.com/rulyotano/mui-profile) (because I’m using Material-Ui). After that just clone it into your local.

Then let’s create the Next.js application. Before continuing, If you like to know more about NextJs, just check this: [What is Next.js?](https://nextjs.org/learn/foundations/about-nextjs/what-is-nextjs), and you also can find here ([Getting Started | Next](https://nextjs.org/docs/getting-started).js) the complete step-by-step guide to start and configure it.

We need to have Node.js installed (12.22.0 or later) and, in my case, I will use `yarn` (you can install `yarn` as another global npm package). As the guide says, just run this command to create it: `yarn create next-app --typescript` . I want to use typescript so I added the option`--typescript` . After installing all the dependencies you will have a complete and ready-to-go NextJs project.

> ***Note:** after running the above command, NextJs will create his files into another directory named with the project name you choosed, which will add an extra depth level. I recommend avoiding this and moving all files and directories to the root folder.*

Now run the app:

```
cd ./your-project-name
yarn dev
```

And that is it. If you had your port 3000 free you should be able to open [http://localhost:3000](http://localhost:3000/) in your browser and see your brand new app.

![](/images/build-your-personal-website-for-free-using-reactjs/1*bekJTXwSgNj3R0_VYdvPiw.png)

## **Let’s customize our web**

Now we have a React.js app ready and now it is up to you. If you go to the `pages` directory, you will find that there is where the pages are defined (currently only the index).

```
└───📁 pages/
    ├───📁 api/
    │   └───...
    ├───📄 index.tsx
    └───📄 _app.tsx
```

The `_app.tsx` file is like a parent to all the pages. You can include here the common code for all the pages. It receives a `Component` from the props which basically is the child page. I use it to add here all the common things, like styles, headers, and so on.

From here, I’m only going to give you some tips based on issues that I had when I was customizing my web with Material-UI.

The first thing we need to configure is the library that we want to use to be able to work properly when doing server rendering. To that, we can use the [“Custom Document”](https://nextjs.org/docs/advanced-features/custom-document), and set up it there. In the latest version of MUI [here is](https://mui.com/material-ui/guides/server-rendering/) what we need to do in order to configure it. In my case, I used the MUI version 4.x but as frontend libraries go so fast, I see now is version 5.x and it brings some breaking changes. This is how it looks in my case:

The key is what we do inside the `.getInitialProps` function. We do whatever we need in order to execute the custom js libraries before generating the HTML, which will depend on the library you want to use and the version.

Another problem I found was that the MUI javascript and ccs were overlapping with already existing ones in the server-side generated HTML. To solve that I just removed those javascript files from the html body. To do that I added the following hook to the `_app.tsx` file:

```
React.useEffect(() => {
  const jssStyles = document.querySelector('#jss-server-side');
  if (jssStyles) {
    jssStyles.parentElement.removeChild(jssStyles);
  }
}, []);
```

## **Having several pages**

To have several pages you need to do a couple of things. First, you need to add it to the `pages` directory. For example, if you add `articles.tsx` to your `pages` directory, that will create a `/articles` route.

Also, in order to work properly with the server-side rendering, I needed to add an entry to the `exportPathMap` method in the `next.config.js` file:

```
exportPathMap: function () {
  return {
    '/': { page: '/' },
    '/articles': { page: '/articles' },   // <---- add this
  };
}
```

You can add more complex routes, like dynamic for example. I recommend reading the [NextJs routing documentation](https://nextjs.org/docs/routing/imperatively).

## **Let’s talk about the content**

I just wanted to avoid using databases and API requests in this project. That is why I just added it to a `.json` file. You can do it as you prefer.

You may store the images in the `public/` directory and then just add a local reference to them:`href="/img/yourimage.png"` or in your data source.

But in my case, I just did a trick I found to use `Google Photos` as an image source. I liked it because:

1. Don’t overload the repository or the web server by exposing them.
2. I can easily request an image in the size I want.

The procedure is the following:

1. Create a google photos album.
2. Share it by creating a public link.
3. Now you can add to the album the images you want to get from your website.
4. Open the album’s link that you already created in step 2 in an incognito web browser.
5. Open any image and right-click and copy the image URL you can use in your content.

Now comes the fun part that Google does for us. You may notice the image URL ends with something like `=w1239-h929-no` , that is the size of the image that I want to get. So, if I just want a small image to show in list items I prefer to get it with `w30` (width 30px) instead.

So, what I do is save the image without that part in my static content data. And then I created a js-helper to get the images in the size I want before rendering:

And then just use it to get the final image url:

```
const imageWithSize = useMemo(() => getGoogleImageWithSize(image, 100), [image]);
===================
<cardmedia component="img" alt="{title}" height="100" image="{imageWithSize}" title="{title}" classname="{classes.image}">
```

After you get your site ready (or at least the first version) you can do `yarn build` in your terminal. This will generate an `out` directory with your website ready to copy to your GitHub Pages. Copy the content to your `github.io` project (you should delete all the previous content before, or at least, override it), commit, and push it. In a few minutes, you should be able to see the new changes on your website.

There is a couple of things that I needed to do here. The first one is to create an empty `.nojekyll` file in the output directory (the root of the website). This is needed to enable javascript code to work properly. Maybe this changed in the latest versions, at least I had this issue.

The next thing I needed to do, was to add a CNAME file to the root of the website, in order to verify the domain name. The content of this file should be your domain name.

In order to get this done automatically when running our `yarn build` command in the terminal, I just modified that command a bit. Go to your `package.json` file and in the section `scripts` override the `build` entry with the following (change `rulyotano.com` by your domain name):

```
"build": "next build && next export && echo ''> ./out/.nojekyll && echo rulyotano.com > ./out/CNAME",
```

This should be enough! But, in order to update my profile webpage do I need to update and commit and push two repositories? In the next section, I will explain how I handled to do this process automatically.

## **Automate your deployment with GitHub Actions**

As the title says, yes, we are going to use GitHub Actions to build, test, copy the files to the `github.io` repo, and push them. I don’t know if you are familiar with GitHub Actions, if not, I just want to say it is a mechanism GitHub created to automate things in your projects. We can use it to implement our CD/CI pipelines (Continous Deployment/Continous Integration).

First, we need to create a GitHub token to authorize the external processes to do changes within our GitHub repositories. To do that, go to your GitHub settings page (top-right corner menu > `Settings`), then to `Developer settings` and finally to `Personal access tokens` (or you can get there just using [this link](https://github.com/settings/tokens)). In this place generate the new access token and save the value. Be careful because when you leave this page you won’t see the value again.

You will add this token to the secrets of your ReactJs website repo. Go to the project’s page and then to `Settings` > `Secrects` > `Actions` and click `New repository secret`. Copy your personal access token and add a name, I used `API_TOKEN_GITHUB` .

The next step is to create the action pipeline. In the same repo, just create a `.yml` file in this location `.github/workflows` . Then you can copy the content from the following file and adapt it to your needs:

After that, if everything is ok, every time your master branch is updated also you will be updating your `github.io` repo and your website. In this way, you will only need to update one repository and it becomes a lot easier.

## **Summary**

As result, from this article, we will get a React.js website, hosted by GitHub pages that we can easily update by accepting a PR or by making a push. I hope you can get something from here. The following links are the projects that I have created and the final result (my personal website) in case you want to use them as guidance:

* [My GitHub page repository](https://github.com/rulyotano/rulyotano.github.io)
* [My profile webpage repository](https://github.com/rulyotano/mui-profile)
* [My personal website](https://rulyotano.com/)
