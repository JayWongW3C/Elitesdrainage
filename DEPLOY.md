# How to put the new site live

This replaces the UENI site with the new one on the same address, elitedrainage.uk. Netlify hosting is free at this size and includes the contact form.

Allow about an hour. The site is offline for at most a few minutes while the domain switches over.

**Before you start:** don't cancel UENI until step 5 is finished and the new site is showing on elitedrainage.uk.

---

## Step 1: Find out who controls the domain

1. Log in to UENI and look for a "Domain" section.
2. If UENI says it registered elitedrainage.uk for you, ask UENI support to **transfer the domain to you** or give you DNS access. Ask for the "EPP / auth code" for a transfer. Without this you cannot point the domain at the new site.
3. If you bought the domain yourself (for example at GoDaddy, 123-reg, Namecheap or IONOS), log in there and confirm you can see a "DNS" or "Manage DNS" page.

## Step 2: Create a Netlify account and connect the site

1. Go to **app.netlify.com/signup** and choose **Sign up with GitHub**. Use the GitHub account that holds the `elitesdrainage` repository.
2. Click **Add new site**, then **Import an existing project**.
3. Choose **GitHub**, then pick the **elitesdrainage** repository.
4. On the settings screen:
   - **Branch to deploy:** the branch this site was built on, or `main` once it has been merged.
   - **Build command:** leave it empty.
   - **Publish directory:** `public` (the `netlify.toml` file already sets this).
5. Click **Deploy**. After about a minute you get a test address such as `something.netlify.app`. Open it and check the site.

## Step 3: Turn on the contact form emails

1. In Netlify, open your site and go to **Forms**. Click **Enable form detection** if it is not already on.
2. Redeploy the site once: go to **Deploys**, then **Trigger deploy**, then **Deploy site**. Netlify needs this to detect the form.
3. Go to **Site configuration**, then **Notifications**, then **Emails and webhooks**, then **Form submission notifications**, then **Add notification**, then **Email notification**.
4. Enter the email address where you want enquiries to arrive.
5. Test it: fill in the form on the netlify.app address and check that the email arrives. Look in spam the first time.

## Step 4: Connect elitedrainage.uk

1. In Netlify go to **Domain management**, then **Add a domain**. Type `elitedrainage.uk` and confirm.
2. Netlify shows the DNS records to add. They are usually:
   - an **A record** for `@` (the bare domain) pointing to `75.2.60.5`
   - a **CNAME record** for `www` pointing to `your-site-name.netlify.app`

   Use the exact values Netlify shows you, because they can change.
3. At your domain provider (step 1), open the DNS settings and **delete the old A and CNAME records that point to UENI**. Then add the new ones. Do not touch any **MX** records: they control email.
4. Wait. The switch-over usually takes 10 minutes to a few hours.
5. Back in Netlify's **Domain management**, under **HTTPS**, click **Verify DNS configuration**, then **Provision certificate**. This gives you the padlock (https).

## Step 5: Check it worked

- `https://elitedrainage.uk` shows the new site.
- `https://elitedrainage.uk/about-us` redirects to `/about/` (this proves the old Google links still work).
- The phone buttons ring the right number on your mobile.
- The contact form sends you an email.

Once all four checks pass, you can cancel UENI hosting. **If UENI holds the domain, finish the transfer first.**

## Step 6: Tell Google (about 20 minutes, free)

1. Go to **search.google.com/search-console** and sign in with your Google account.
2. Click **Add property** and choose **Domain**. Enter `elitedrainage.uk`.
3. Google gives you a TXT record. Add it in your domain DNS settings, the same place as step 4, then click **Verify**.
4. Open **Sitemaps** on the left, enter `sitemap.xml` and click **Submit**.
5. Open **URL inspection** and paste `https://elitedrainage.uk/`, then click **Request indexing**. Do the same for the blocked drains page: `https://elitedrainage.uk/services/blocked-drain-clearing/`.

After 2 to 4 weeks Search Console shows which searches bring people to the site.

## Step 7: Google Business Profile (the biggest win for local calls)

Follow the "Week 2" section of the SEO audit. In short:

1. Go to **google.com/business**. Claim or create the profile for **Elite Drainage Services**.
2. Set the main category to **Drainage service**.
3. Use exactly the same name, phone number (0330 633 0336) and website (https://elitedrainage.uk) as the site.
4. Add your service areas (the same towns as the website), your hours and at least 10 real job photos.
5. After each job, text the customer your review link, which you'll find in the profile under "Ask for reviews".

---

### If something goes wrong

- **The site shows "Page not found" on Netlify:** check that the publish directory is `public`.
- **The form does nothing:** make sure form detection is on (step 3) and that you redeployed after turning it on.
- **The domain still shows the UENI site after 24 hours:** there is usually an old UENI record left in DNS. Remove every A, AAAA and CNAME record for `@` and `www` that is not Netlify's.
- **Email stopped working:** an MX record was changed or deleted. Put it back to the value your email provider gives you.
